import asyncio
import contextlib
import importlib.util
import io
import json
import tempfile
import unittest
from collections import Counter
from pathlib import Path
from unittest.mock import AsyncMock, patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "generate_dictation.py"
spec = importlib.util.spec_from_file_location("generate_dictation", SCRIPT)
dictation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dictation)


class DictationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.sentences = ["Vandaag leer ik Nederlands."] * 15
        self.output = self.root / "dictation"

    def test_all_sizes_use_three_balanced_voices_at_normal_speed(self):
        for count in range(15, 21):
            for seed in range(10):
                plan = dictation.make_plan(self.sentences[:1] * count, seed)
                counts = Counter(item["voice"] for item in plan["items"])
                self.assertEqual(set(counts), set(dictation.VOICES))
                self.assertLessEqual(max(counts.values()) - min(counts.values()), 1)
                self.assertEqual(plan["rate"], "+0%")
                self.assertEqual(
                    [item["file"] for item in plan["items"]],
                    [f"{index:02d}.mp3" for index in range(1, count + 1)],
                )
        self.assertNotEqual(
            dictation.make_plan(self.sentences, 1)["items"],
            dictation.make_plan(self.sentences, 2)["items"],
        )

    def test_input_limits_and_utf8_bom_blank_lines(self):
        source = self.root / "dictation.txt"
        source.write_text("\ufeff" + "\n\n".join(self.sentences), encoding="utf-8")
        self.assertEqual(dictation.read_sentences(source), self.sentences)
        for count in (0, 14, 21):
            source.write_text("\n".join(self.sentences[:1] * count), encoding="utf-8")
            with self.assertRaises(ValueError):
                dictation.read_sentences(source)

    def test_dry_run_writes_nothing_and_seed_reproduces_preview(self):
        preview = dictation.prepare_plan(self.sentences, self.output, 42, True)
        self.assertFalse(self.output.exists())
        actual = dictation.prepare_plan(self.sentences, self.output, 42, False)
        self.assertEqual(preview, actual)
        self.assertEqual(
            dictation.prepare_plan(self.sentences, self.output, None, False), actual
        )

    def test_changed_text_seed_and_unmanaged_files_are_preserved(self):
        dictation.prepare_plan(self.sentences, self.output, 42, False)
        manifest = self.output / "manifest.json"
        original = manifest.read_bytes()
        changed = self.sentences.copy()
        changed[0] = "Morgen ga ik naar Amsterdam."
        with self.assertRaises(ValueError):
            dictation.prepare_plan(changed, self.output, None, False)
        with self.assertRaises(ValueError):
            dictation.prepare_plan(self.sentences, self.output, 43, False)
        self.assertEqual(manifest.read_bytes(), original)
        other = self.root / "other"
        other.mkdir()
        recording = other / "01.mp3"
        recording.write_bytes(b"existing recording")
        with self.assertRaises(ValueError):
            dictation.prepare_plan(self.sentences, other, None, False)
        self.assertEqual(recording.read_bytes(), b"existing recording")

    def test_network_failure_cleanup_and_resume_keep_finished_audio(self):
        plan = dictation.prepare_plan(self.sentences, self.output, 42, False)
        calls = []

        async def failing_service(text, voice, target):
            calls.append(voice)
            target.write_bytes(b"partial audio")
            if len(calls) > 1:
                raise ConnectionError("test outage")

        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            with patch.object(dictation, "synthesize", side_effect=failing_service):
                with patch.object(dictation.asyncio, "sleep", new_callable=AsyncMock):
                    with self.assertRaises(RuntimeError):
                        asyncio.run(dictation.generate(plan, self.output))
        self.assertEqual(len(calls), 4)  # One success, then three attempts.
        self.assertEqual(
            {path.name for path in self.output.iterdir()}, {"manifest.json", "01.mp3"}
        )
        finished = self.output / "01.mp3"
        timestamp = finished.stat().st_mtime_ns
        resumed = dictation.prepare_plan(self.sentences, self.output, None, False)
        self.assertEqual(resumed, plan)

        async def working_service(text, voice, target):
            target.write_bytes(b"finished audio")

        with contextlib.redirect_stdout(io.StringIO()):
            with patch.object(dictation, "synthesize", side_effect=working_service) as service:
                asyncio.run(dictation.generate(resumed, self.output))
        self.assertEqual(service.call_count, 14)
        self.assertEqual(finished.stat().st_mtime_ns, timestamp)
        self.assertEqual(len(list(self.output.glob("*.mp3"))), 15)
        self.assertEqual(json.loads((self.output / "manifest.json").read_text()), plan)


if __name__ == "__main__":
    unittest.main()
