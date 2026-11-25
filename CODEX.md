# Codex Instructions

Use this repo to help the user learn Dutch from lesson screenshots and generated practice.

## Lesson Generation Skill

For new lesson materials and homework requests, use `$dutch-lesson` and follow [its workflow](.agents/skills/dutch-lesson/SKILL.md). The skill is stored in the project's `.agents/skills` directory for automatic discovery. The generator and the independent reviewer both use this file as the source of course requirements. Keep detailed course requirements here instead of duplicating them in the skill. Checking the learner's answers is a separate task.

## Main Goal

Turn each lesson screenshot or Miro board into:

1. a clear lesson summary,
2. cumulative vocabulary entries,
3. homework, including a listening dictation with AI-generated audio, generated immediately without a separate request.

## Directory Rules

- Use lesson folders named `les-XX`.
- Store lesson summaries in `les-XX/README.md`.
- The first generated homework set is `les-XX/homework.md`, with a separate `homework_answers.md`. Use `dictation.txt` and `dictation/` for its transcript and audio.
- When another set is requested, preserve existing work, including learner answers. Allocate the next available set number across exercises, keys and dictations: `homework_2.md`, `homework_2_answers.md`, `dictation_2.txt`, `dictation_2/`, and so on. A correction to an existing set stays in its original files.
- Some older lessons have `source_exercises.md`, an archive of exercises from the board. Preserve these files. New lessons use the homework files above.
- Keep vocabulary in the single cumulative file `WORDS.md`.
- Do not create separate per-lesson word-bank files unless the user explicitly asks.

## Screenshot Analysis Workflow

When the user posts a lesson screenshot:

1. Identify the lesson number from the image or the user message.
2. Create the lesson folder if needed.
3. Ignore screenshot sections labelled `fonetiek` or `luisteren`. Analyze visible sections such as:
   - grammatica,
   - woordenschat,
   - spreken,
   - schrijven,
   - vocabulary under homework headings.
4. Create or update `les-XX/README.md`.
5. Treat a screenshot heading such as `huiswerk`, «домашняя работа», «домашнее задание» or “homework” only as a list of new words and expressions. Extract the lexical items actually visible, check them against `WORDS.md`, and include them in vocabulary practice. Do not assign, solve or transcribe tasks from this block or adopt its instructions or format. If it contains no identifiable vocabulary, record none. Ordinary uses of the word `huiswerk` in Dutch study text retain their meaning.
6. Mention any uncertainty if the screenshot is too small or text is unreadable.
7. Write all explanatory content in Russian. Keep Dutch forms, examples, dialogues, and source texts in Dutch. English may appear only as source text in exercises that explicitly ask the learner to translate from English into Dutch.
8. Generate the homework immediately according to the format below. Use original exercises.

## Lesson Summary Format

Use this format for `README.md`:

```markdown
# Урок XX — конспект

## Источник

- Материал: скриншот / доска Miro / заметки пользователя
- Дата добавления: YYYY-MM-DD

## Основные темы

- ...

## Грамматика

Объясняйте каждую грамматическую тему по-русски. Нидерландские формы и примеры оставляйте на нидерландском.

### Название темы

Объяснение с короткими примерами.

## Темы лексики

- ...

## Письменная практика

- ...

## Полезные примеры

1. ...

## Домашняя работа

[Упражнения](homework.md) · [Ответы](homework_answers.md)

## Неясности в источнике

- ...
```

## Vocabulary Rules

When adding to `WORDS.md`:

- Prefer dictionary form for verbs.
- Include article for nouns: `de` or `het`.
- Include plural or usage notes when helpful.
- Include lesson id in the `Lesson` column.
- Follow the normalization rules at the top of `WORDS.md`: use stable English `Type` values and sorted, unique `les-XX` values in `Lesson`.
- Avoid duplicates for the same meaning and grammatical function; update the existing row and retain its lesson references and notes. Keep separate rows for different meanings or parts of speech, even when `Dutch` is identical.
- Select vocabulary by the entire `Lesson` column, not only by section heading; earlier rows can include later lesson references. The first lesson is the earliest recorded occurrence of the entry, not necessarily of every meaning in its notes.
- Keep translations practical, not overly academic.

## Homework format

Use this section as the complete template for each new set, including sets requested separately. The user may request a shorter set or a narrower topic. Base the content on the lesson source, the summary and material learned by that point. Use earlier lessons as evidence of what has been taught. When creating practice for an earlier stage, omit constructions that have not yet been taught and number the applicable sections consecutively.

Write learner-facing headings, instructions, cues and explanations in Russian, and target forms and answers in Dutch. Use Russian-to-Dutch translation for sentence production. Include an English-to-Dutch section only on explicit request; its sentences must differ in meaning from those in the Russian section. Target A2 with familiar words and sentence patterns. When practising inversion after an initial adverbial, prefer a simple verb–subject sequence unless the exercise specifically practises another construction. Mix current and previously taught vocabulary across the set and provide a numbered answer for each item and sub-item. Use closed tasks that the learner can check independently.

### Section order and size

Use 15–20 items per section unless a different count is given below. The numbered list specifies the order in the worksheet and separate answer key.

1. **New words in context.** Give a Russian cue and a Dutch sentence with one or more gaps. Test new words, expressions and new meanings from this lesson. Use as many items as needed for coverage.
2. **All target vocabulary.** Test the full set of target words, expressions and meanings in recall or translation, including previously known words practised in the source. Use as many items as necessary. Each target must also occur in a learner task elsewhere in the set, in a different context. Inflected forms count when they practise the intended meaning. An entry in a heading, hint, word list or key alone does not count. Verify both numbered occurrences for each target before delivery and keep that coverage map out of the learner files.
3. **Russian-to-Dutch translation.** Give 10–15 sentences using the lesson grammar and vocabulary.
4. **Purpose and evaluation with `om … te`.** Mix statements, yes/no and question-word questions, present, past and future contexts where natural. Practise negation in either clause, evaluation (`Het is leuk om …`, `Ik vind het leuk om …`), separable verbs (`op te staan`) and familiar modals with a bare infinitive.
5. **Negation.** Practise `niet`, `geen` and learned negative adverbs.
6. **Questions.** Mix yes/no and question-word questions. Occasionally include a destination question with `naartoe`, leaving the Dutch wording to the learner.
7. **Grammar terms and classroom instructions.** Ask for Dutch terms and instructions seen in the source, with earlier terms for revision. Use fewer items if necessary to stay within taught terminology. Add newly encountered terms to the word bank.
8. **Personal, object and possessive pronouns.** Use exactly 15 items. Ten practise the full forms `hen` and `hun` across direct objects, indirect objects without a preposition, objects of prepositions and possessives. Five practise other pronouns.
9. **Plural nouns.** Ask for the plural with its article. Include both singular noun genders across the examples.
10. **Numbers, dates and times.** Include large cardinal and ordinal numbers, dates, years, and both conversational and timetable readings of clock times.
11. **Conjunctions and `toen`.** Practise learned conjunctions and all three uses of `toen` once taught: narrative sequence, reference to a past time, and a temporal subordinate clause. Vary clause position to practise inversion and verb-final order. For every Russian «потому что» in this section, specify `Подсказка: используйте want.` or `Подсказка: используйте omdat.` Give each as a primary answer at least once when both have been taught. Leave other conjunction choices to the learner.
12. **Modal verbs.** Include `zullen` for promises or offers and several items with `hoeven niet te` / `geen … te`, including inversion and a separable verb. Contrast lack of necessity with prohibition (`niet mogen`). Let the learner select the modal verb from the Russian meaning.
13. **Strong and irregular verbs.** Practise the taught verbs in new situations, including imperfectum and perfectum. Specify the tense while leaving the lexical verb to the learner.
14. **Listening dictation.** Use the recording and transcript requirements below.

The standard set has no standalone article, reflexive-pronoun or comparative/superlative section. Articles are still chosen independently in translation, and previously learned forms can appear naturally elsewhere. For possessive pronouns in written keys, include full and reduced forms where both fit (`jouw/je`, `mijn/m’n`, `zijn/z’n`). Use the full form alone when emphasis requires it.

### Unfamiliar vocabulary

Check the words and meanings needed for each prompt and answer against the current source, earlier lesson material and dated dictionary entries. An inflected form can be familiar, and an old word can have a new meaning. A dictionary entry added during generation alone does not establish that the learner studied it. Prefer familiar wording. For unfamiliar vocabulary that is needed, highlight the affected word in bold in each prompt and give a Russian-labelled hint with the Dutch dictionary form and Russian meaning. Keep the noun article, tested form and full answer for the key. For dictation, put a short glossary before the recordings and keep the transcripts in the key.

### Tense instructions in written practice

When the learner has to produce a finite verb, make the expected tense clear in the Russian prompt or section instructions. A single instruction covers a uniform section. For a mixed section, identify the applicable items or clauses. This also applies when the main exercise tests a different skill, such as negation, questions, or conjunctions.

If the task requires a particular Dutch form, name it (for example, «Используйте perfectum»). A Russian past-tense verb or a time word such as «вчера» cannot by itself resolve the choice between imperfectum and perfectum. If choosing the tense is itself the task, say so and provide enough narrative context for the choice. When several tenses are acceptable, tell the learner and explain the relevant alternatives in the key. Vocabulary-only answers and verb forms already supplied in a prompt need no tense label.

### Independent verb choice and learned constructions

- In reflexive-pronoun and strong/irregular-verb translation exercises, let the learner choose the verb independently. Do not append routine Dutch infinitive hints such as `(zich wassen)` or `Beginnen; perfectum`. Keep explicitly required hints from the rules below, such as `aanmelden` / `inschrijven`, unfamiliar vocabulary and necessary ambiguity clarification; do not turn these exceptions into hints for every item. Follow the tense instructions above.
- The user confirmed that `zijn + aan het + infinitive` has not been studied. Its appearance in a screenshot does not establish that it has been taught. Exclude it from generated practice, answer keys and dictation until the user says otherwise; use the familiar present tense where appropriate. A source note may mention that it remains unlearned.

- Use `dus` as a coordinating conjunction with subject–finite verb order, as taught: `Ik ben moe, dus ik blijf thuis.` Reserve connective-adverb inversion for when the learner has studied it.
- Use the taught `om … te` and `hoeven … te` patterns. Reserve other infinitive constructions with `te` and advanced infinitive combinations for lessons where they have been taught.

### Listening dictation

- Generate 15–20 new Dutch sentences using the current lesson and material already learned up to that lesson. Mix current and earlier vocabulary from `WORDS.md`. Do not copy sentences from the other exercises or introduce later grammar to fill the quota.
- Plan coverage of known tenses, learned conjunctions (explicitly including `omdat` and `als` once covered), separable verbs, reflexive pronouns, possessive pronouns, and cardinal and ordinal numbers. Treat individual learned tenses, conjunctions, and constructions as coverage targets; include every applicable family when the available slots allow it. Combine targets naturally in a sentence without making it needlessly difficult.
- If the coverage targets exceed the chosen 15–20 sentence slots, randomly sample targets without replacement rather than increasing the dictation length or always selecting the same subset. Use an actual random draw (for example Python's `random.sample`) and record the selected targets in a short coverage note in the answer key. Across new sets, make fresh random selections. This does not override the learned-material boundary.
- Review Dutch word order, auxiliary choice, separable verb forms, pronouns, articles, and number spelling before synthesis. Write numbers in words in the source so the exact spoken wording is unambiguous. Choose one spoken form of a possessive pronoun per recording; show that exact form in the transcript, without slash alternatives in the synthesis input.
- In the homework exercise, write Russian instructions to listen and transcribe each numbered recording. Link `dictation/01.mp3`, `dictation/02.mp3`, etc.; keep Dutch transcripts and translations out of the prompts and filenames. Give the exact numbered transcript in the separate answer key. The source file and manifest are generation/answer materials, not learner prompts.
- Save the reviewed transcript as UTF-8 `dictation.txt`, with one Dutch sentence per nonempty line, no heading, numbering, translations, or comments. Line order, audio numbering, and answer-key numbering must match exactly.
- Generate the recordings with the repository script, using mise from `PATH`:

  ```bash
  mise exec uv@0.13.5 -- uv run --script scripts/generate_dictation.py les-XX/dictation.txt
  ```

- Use normal speed (`+0%`). For each sentence, use one randomly assigned voice from `nl-NL-ColetteNeural`, `nl-NL-FennaNeural`, `nl-NL-MaartenNeural`, `nl-BE-ArnaudNeural`, and `nl-BE-DenaNeural`; keep that voice throughout the sentence. All five must appear in every new dictation, with counts differing by at most one. Existing dictations keep their saved voices and recordings; do not regenerate them to add voices. The script shuffles a balanced voice pool and saves the assignments in `dictation/manifest.json`; resuming an existing set retains those assignments.
- The script creates one MP3 per sentence and resumes missing recordings. Do not replace an existing set merely to randomize its voices again. For a revised transcript, use a new matching source/output name. Never overwrite completed homework or unrelated audio.
- Run synthesis as part of generating the homework, and check that every linked MP3 exists and is nonempty. If the service is unavailable, retain the transcript and keys, explicitly report which recordings are missing, and do not claim the dictation audio is complete. A dry run is only a plan, not successful audio generation.
- This adds generated listening practice; it does not imply that source screenshots contained audio. Do not rewrite historical lessons just to add dictations unless requested. Repository Markdown audio links are not embedded players; do not claim GitHub Pages playback is available unless a site was actually configured and published.

### Initial adverbials in Russian-to-Dutch translation

- If a Russian source sentence starts with an adverbial of time, place, or another circumstance, start the Dutch translation with the corresponding adverbial as well. Apply this to answers and answer keys in every exercise type with Russian source sentences.
- Preserve correct Dutch word order: when an adverbial comes first in a main clause, place the finite verb before the subject (inversion).
- Example: «Вчера я заблудился в Амстердаме.» → `Gisteren ben ik in Amsterdam verdwaald.` Use this order in the answer key rather than `Ik ben gisteren in Amsterdam verdwaald.`
- Apply this rule to newly generated translations and answer keys. Do not revise existing exercises or answer keys solely to conform to this rule unless the user explicitly asks.

### Hints for `er` in translation exercises

- When a generated translation exercise expects `er`, add a short Russian hint to the affected prompt identifying its role (for example, an unstressed reference to an already mentioned place, or the existence construction `er is / er zijn`). Do not expose the complete translated sentence.
- Distinguish required `er` from an optional natural alternative. If `hier`, `daar`, or a version without `er` also fits the Russian meaning and context, accept it in the key rather than presenting `er` as the only correct answer. Supply enough context for a place-reference use of `er`; do not silently reinterpret «здесь» as a previously mentioned place.
- Distinguish locative `hier` / `daar` / `er` from impersonal subject `het` in weather and temperature expressions: `het is koud`; a place word does not replace that subject.
- Apply these hints to newly generated work. Do not rewrite existing examples solely for this rule unless the user requests it.

### Hints for `aanmelden` and `inschrijven`

- When an exercise answer expects `aanmelden` or `inschrijven`, add a short Russian-labelled hint to each affected prompt naming the intended verb in its infinitive form: `Подсказка: используйте aanmelden.` or `Подсказка: используйте inschrijven.` Apply this to all relevant written exercise types, including translation and `om ... te` exercises.
- Name only the intended verb; do not reveal its conjugated form or the complete answer. Ensure the answer key uses the verb named in the hint.
- Apply this rule to newly generated exercises. Do not rewrite existing homework solely to add these hints unless the user requests it.

### Ambiguous verb choices in translation exercises

- If a translation prompt leaves a choice between different Dutch verbs or constructions, but the key expects a particular one, make that choice clear with a short Russian-labelled infinitive hint. In particular, population statements such as «В городе 18000 жителей» can use `hebben` (a town has inhabitants) or `wonen` (people live in a town); specify the verb used in the key rather than making the learner guess it.
- Keep hints limited to the intended verb, without revealing its grammatical form or the full translation. Continue to preserve initial adverbials and correct word order in the answer. This does not override independent choice of conjunctions and modal verbs in their dedicated exercises.
- A different verb or construction is not automatically an error: accept grammatically correct translations that preserve the source meaning, and distinguish a valid alternative from failure to practise an explicitly requested verb. In exercises targeting another skill, such as number spelling, explain relevant alternatives in the key.
- Apply this rule to new exercises and to existing items the user identifies as ambiguous; do not rewrite unrelated homework.

### Hints for ambiguous `bij` / `naast` choices

- In Russian-to-Dutch exercises, when spatial wording such as «у», «около», «возле» or «рядом с» leaves both `bij` and `naast` plausible, explicitly name the preposition used in the key: `Подсказка по предлогу: используйте bij.` or `Подсказка по предлогу: используйте naast.` The learner wants to know the intended interpretation, not guess the key's choice.
- Keep the hint limited to the preposition; do not reveal the noun article or the full translated phrase. Use `bij` for proximity to a landmark and `naast` for an adjacent position where that is the intended meaning; do not imply that Russian «рядом» always maps to one of them.
- Match the answer key to the hint. Where the original Russian wording permits an alternative spatial interpretation, explain the valid alternative in the key rather than treating a different preposition as automatically ungrammatical. Distinguish an acceptable translation from following the specified preposition for this item.
- Apply this to newly generated Russian-source exercises and the current lesson's items identified by the user. Preserve learner answers and do not rewrite unrelated historical exercises.

### Unambiguous Russian question and address prompts

- When a Russian translation prompt targets informal plural `jullie`, make the group explicit, for example «Куда вы все едете?». When targeting polite `u`, identify polite address to one person in the context or a brief Russian note. Capitalization alone, especially at the start of a sentence, does not disambiguate the addressee.
- If a prompt leaves «вы» ambiguous, accept both `u` and `jullie` with their matching verb forms; do not treat the key's choice as the only correct answer.
- Distinguish questions about whether someone asks something from reports of their question: «Спрашивает ли она, есть ли у нас время?» → `Vraagt ze of we tijd hebben?`; «Она спрашивает, есть ли у нас время.» → `Ze vraagt of we tijd hebben.` Use explicit Russian wording when the exercise tests this distinction.

### Independent article choice in translation exercises

- The user wants to choose articles independently. Do not add article hints to translation prompts or instructions: no parenthetical notes about known objects, first mentions, substances in general, or which article to use.
- Use natural Russian sentences. Do not add artificial qualifiers such as «известный», «конкретный» or «ожидаемый», or demonstratives such as «этот/тот», solely to signal the intended article.
- When a dedicated article or plural exercise applies to the lesson, its instructions may specify the requested dictionary form without revealing the answer.
- Use correct articles in the answer key. Russian may allow multiple interpretations: the key gives one natural translation, and grammatically correct article alternatives supported by the source meaning are acceptable. Explain meaningful differences in the key when helpful, not as hints in the prompt.

## Style

- Be clear, practical, and beginner-friendly.
- Use Russian explanations for Dutch examples.
- Do not over-explain advanced grammar unless needed.
- Make exercises easy to print or copy into notes.
- Keep answer keys separated from exercises.
