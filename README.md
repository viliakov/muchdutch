# MuchDutch A0

Personal Dutch learning repo for turning lesson screenshots into structured notes, vocabulary, and extra homework.

## Structure

```text
.
├── README.md
├── WORDS.md
├── CODEX.md
├── les-01
│   └── README.md
├── les-02
│   └── README.md
├── les-03
│   └── README.md
├── les-04
│   └── README.md
├── les-05
│   └── README.md
├── les-06
│   ├── README.md
│   └── homework.md
└── les-07
    ├── README.md
    └── homework.md
```

Each lesson folder should be named `les-XX`, for example `les-01`, `les-02`, `les-06`.

## Lesson Files

Each `les-XX` folder can contain:

- `README.md`: lesson summary generated from screenshots or notes.
- `homework_extra.md`: additional exercises generated automatically from the lesson summary and cumulative word bank, including a grammar-terminology exercise and answer keys.
- `homework.md`: historical lesson homework; homework already visible in screenshots is no longer duplicated.
- `materials.md`: optional manual notes, links, or transcript fragments.
- `dictation.txt`: 15–20 Dutch sentences for listening dictation, one per line; this is the transcript/answer material.
- `dictation/`: numbered MP3 recordings and `manifest.json` with the text, random voice assignments, and normal-speed settings.
- `screenshots/`: optional source images if they are added to the repo later.

The most important file is `README.md`. It should capture what was learned in the lesson, especially grammar, vocabulary themes, pronunciation, listening/speaking topics, and common example sentences.

## Vocabulary

`WORDS.md` is the cumulative word bank for the whole course. New words from every lesson should be added there instead of keeping separate vocabulary lists per lesson.

This makes later exercises richer: homework for `les-06` can use words from earlier lessons, while still prioritizing the new material from the current lesson.

## Workflow

1. Post a screenshot of a Miro board or lesson material to Codex.
2. Codex analyzes the screenshot and creates or updates `les-XX/README.md`.
3. Codex adds new vocabulary to `WORDS.md`.
4. Codex immediately generates `les-XX/homework_extra.md`, without a separate request, using:
   - the current lesson summary,
   - grammar learned so far,
   - the cumulative vocabulary in `WORDS.md`,
   - pronunciation patterns visible in the lesson material.
5. Every generated homework set includes a dedicated exercise testing Dutch grammar terms and exercise instructions from the screenshots, with Russian prompts and an answer key. Homework already present in a screenshot is not transcribed again.
6. Every new homework set also includes a listening dictation of 15–20 sentences covering learned grammar. Recordings use all three Dutch voices in random order at normal speed; the exact transcript appears in the separate answer key. Existing lessons are not retroactively rewritten.

## Generate dictation audio

With `mise` in `PATH`, run from the repository root:

```bash
mise exec uv@0.13.5 -- uv run --script scripts/generate_dictation.py les-30/dictation.txt
```

Replace `les-30/dictation.txt` with your actual source path. Create this UTF-8 file first: 15–20 Dutch sentences, one per nonempty line, without numbering, headings, or translations. Write numbers in words. The script synthesizes supplied sentences; the lesson-generation workflow chooses grammar topics and writes the sentences according to `CODEX.md`.

The command installs the declared edge-tts dependency through uv automatically. An internet connection is required: text is sent to Microsoft Edge's online speech service. No API key is needed. Each sentence gets one of `nl-NL-ColetteNeural`, `nl-NL-FennaNeural`, and `nl-NL-MaartenNeural`. The distribution is randomized and balanced so all three voices are used. Speech rate stays at `+0%`.

The output folder defaults to the source filename without `.txt`, for example `les-30/dictation/`, containing `01.mp3` through `15.mp3`–`20.mp3` and `manifest.json`. There is one recording per sentence; no combined track is generated. Link these recordings in the homework and keep the transcript in the answer key. A repository Markdown link does not embed an audio player; browser playback on GitHub Pages requires publishing a separate page.

To inspect the plan without generating audio or writing output files:

```bash
mise exec uv@0.13.5 -- uv run --script scripts/generate_dictation.py les-30/dictation.txt --seed 42 --dry-run
```

Use the same `--seed 42` when generating to keep that preview's voice assignments. Without a seed, a fresh set uses a new random assignment. Repeating a command resumes missing or empty recordings and keeps existing nonempty MP3 files and saved voice assignments. Failed requests are retried up to three times; incomplete temporary audio is not saved as a finished MP3.

For a changed transcript or another homework set, use a new source name (for example `dictation_extra2.txt`) or a new `--output` folder. The script refuses to mix changed text or settings with an existing set.

See `CODEX.md` for the detailed instructions Codex should follow.
