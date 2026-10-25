# /// script
# requires-python = ">=3.9"
# dependencies = ["edge-tts==7.3.1"]
# ///
"""Generate a Dutch dictation via mise exec uv@0.13.5 -- uv run --script."""

import argparse
import asyncio
import json
import random
import secrets
import sys
import tempfile
from pathlib import Path
from typing import Optional


VOICES = (
    "nl-NL-ColetteNeural",
    "nl-NL-FennaNeural",
    "nl-NL-MaartenNeural",
)
RATE = "+0%"


def read_sentences(source: Path) -> list[str]:
    sentences = [
        line.strip()
        for line in source.read_text(encoding="utf-8-sig").splitlines()
        if line.strip()
    ]
    if not 15 <= len(sentences) <= 20:
        raise ValueError(
            f"Нужно 15–20 предложений, по одному на строку; получено {len(sentences)}."
        )
    return sentences


def make_plan(sentences: list[str], seed: int) -> dict:
    rng = random.Random(seed)
    # Randomize which voices get the extra slots as well as sentence order.
    voices = list(VOICES)
    rng.shuffle(voices)
    assignments = [voices[index % len(voices)] for index in range(len(sentences))]
    rng.shuffle(assignments)
    return {
        "schema_version": 1,
        "engine": "edge-tts",
        "engine_version": "7.3.1",
        "rate": RATE,
        "seed": seed,
        "items": [
            {"number": index, "text": text, "voice": voice, "file": f"{index:02d}.mp3"}
            for index, (text, voice) in enumerate(zip(sentences, assignments), start=1)
        ],
    }


def prepare_plan(
    sentences: list[str], output: Path, seed: Optional[int], dry_run: bool
) -> dict:
    manifest = output / "manifest.json"
    if manifest.exists():
        saved = json.loads(manifest.read_text(encoding="utf-8"))
        if not isinstance(saved, dict) or type(saved.get("seed")) is not int:
            raise ValueError(f"Некорректный manifest: {manifest}")
        if seed is not None and seed != saved["seed"]:
            raise ValueError("Для другого seed укажите новую папку через --output.")
        plan = make_plan(sentences, saved["seed"])
        if saved != plan:
            raise ValueError(
                "Текст или настройки отличаются от сохранённого набора. "
                "Используйте новый файл диктанта или новую папку через --output."
            )
        return plan

    if output.exists() and any(output.iterdir()):
        raise ValueError(f"Папка {output} не пуста и не содержит manifest.json.")
    plan = make_plan(sentences, seed if seed is not None else secrets.randbits(64))
    if not dry_run:
        output.mkdir(parents=True, exist_ok=True)
        # Keep the plan before synthesis, so retries retain the same voices.
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=output, suffix=".json.part", delete=False
        ) as temporary:
            temp_path = Path(temporary.name)
            try:
                json.dump(plan, temporary, ensure_ascii=False, indent=2)
                temporary.write("\n")
            except BaseException:
                temp_path.unlink(missing_ok=True)
                raise
        try:
            temp_path.replace(manifest)
        finally:
            temp_path.unlink(missing_ok=True)
    return plan


async def synthesize(text: str, voice: str, target: Path) -> None:
    import edge_tts

    await edge_tts.Communicate(text, voice, rate=RATE).save(str(target))


async def save_item(item: dict, output: Path) -> None:
    target = output / item["file"]
    for attempt in range(3):
        with tempfile.NamedTemporaryFile(dir=output, suffix=".mp3.part", delete=False) as temporary:
            temp_path = Path(temporary.name)
        try:
            await synthesize(item["text"], item["voice"], temp_path)
            if temp_path.stat().st_size == 0:
                raise RuntimeError("Сервис вернул пустую запись.")
            temp_path.replace(target)
            return
        except Exception as error:
            if attempt == 2:
                raise RuntimeError(
                    f"Не удалось создать {target.name}: {error}. "
                    "Повторите ту же команду для продолжения."
                ) from error
            print(f"{target.name}: повторная попытка {attempt + 2}/3…", file=sys.stderr)
            await asyncio.sleep(2 ** (attempt + 1))
        finally:
            temp_path.unlink(missing_ok=True)


async def generate(plan: dict, output: Path) -> None:
    for item in plan["items"]:
        target = output / item["file"]
        if target.is_file() and target.stat().st_size > 0:
            status = "уже готово"
        else:
            await save_item(item, output)
            status = "сохранено"
        print(
            f"{item['number']:02d}/{len(plan['items'])}: {item['voice']} — {status}",
            flush=True,
        )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Озвучить 15–20 нидерландских предложений тремя случайными голосами."
    )
    parser.add_argument("source", type=Path, help="UTF-8 файл, одно предложение на строку")
    parser.add_argument("--output", type=Path, help="Папка MP3 (по умолчанию имя файла без .txt)")
    parser.add_argument("--seed", type=int, help="Число для воспроизводимого распределения голосов")
    parser.add_argument("--dry-run", action="store_true", help="Показать план без записи файлов и озвучки")
    args = parser.parse_args()
    try:
        if args.source.suffix.lower() != ".txt":
            raise ValueError("Исходный файл должен иметь расширение .txt.")
        sentences = read_sentences(args.source)
        output = args.output if args.output is not None else args.source.with_suffix("")
        plan = prepare_plan(sentences, output, args.seed, args.dry_run)
        if args.dry_run:
            print(json.dumps(plan, ensure_ascii=False, indent=2))
        else:
            asyncio.run(generate(plan, output))
            print(f"Готово: {len(sentences)} записей в {output}")
        return 0
    except KeyboardInterrupt:
        print("\nОстановлено. Повторите ту же команду для продолжения.", file=sys.stderr)
        return 130
    except Exception as error:
        print(f"Ошибка: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
