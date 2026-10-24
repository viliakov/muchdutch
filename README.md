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

See `CODEX.md` for the detailed instructions Codex should follow.
