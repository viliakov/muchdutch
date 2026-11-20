# Codex Instructions

Use this repo to help the user learn Dutch from lesson screenshots and generated practice.

## Lesson Generation Skill

For new lesson materials and additional-homework requests, use `$dutch-lesson` and follow [its workflow](.agents/skills/dutch-lesson/SKILL.md). The skill is stored in the project's `.agents/skills` directory for automatic discovery. It reads this file as the single source of project requirements and reviews the generated content before delivery. Keep detailed course requirements here instead of duplicating them in the skill. Checking the learner's answers is a separate task.

## Main Goal

Turn each lesson screenshot or Miro board into:

1. a clear lesson summary,
2. cumulative vocabulary entries,
3. additional homework exercises, including a listening dictation with AI-generated audio, generated immediately without a separate request.

## Directory Rules

- Use lesson folders named `les-XX`, for example `les-01`, `les-06`.
- Store lesson summaries in `les-XX/README.md`.
- Do not transcribe or duplicate homework already present in a screenshot. Existing `les-XX/homework.md` files are historical material; keep them unless the user asks to change them.
- Store extra practice tasks that you generate in `les-XX/homework_extra.md`.
- Store dictation source sentences in `les-XX/dictation.txt` and generated recordings in `les-XX/dictation/`. For numbered extra homework, use matching names such as `dictation_extra2.txt` and `dictation_extra2/`; preserve existing sets and user answers.
- Keep vocabulary in the single cumulative file `WORDS.md`.
- Do not create separate per-lesson word-bank files unless the user explicitly asks.

## Screenshot Analysis Workflow

When the user posts a lesson screenshot:

1. Identify the lesson number from the image or the user message.
2. Create the lesson folder if needed.
3. Analyze visible sections such as:
   - grammatica,
   - woordenschat,
   - fonetiek,
   - luisteren,
   - spreken,
   - schrijven,
   - huiswerk.
4. Create or update `les-XX/README.md`.
5. Add new words and reusable phrases to `WORDS.md`.
6. Mention any uncertainty if the screenshot is too small or text is unreadable.
7. Write all explanatory content in Russian. Keep Dutch forms, examples, dialogues, and source texts in Dutch. English may appear only as source text in exercises that explicitly ask the learner to translate from English into Dutch.
8. Immediately create additional practice in `les-XX/homework_extra.md` using the homework rules below; do not wait for a separate request or confirmation. Do not duplicate the screenshot's homework in another file or in the summary.

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

## Произношение

- ...

## Аудирование и устная речь

- ...

## Письменная практика

- ...

## Полезные примеры

1. ...

## Дополнительная домашняя работа

- [Упражнения и ответы](homework_extra.md)

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

## Homework Generation Rules

When processing a lesson screenshot, generate extra homework immediately. Apply the same rules when the user separately asks for homework:

1. Generate `les-XX/homework_extra.md` with additional practice to reinforce the lesson. Do not reproduce the screenshot's `huiswerk` tasks or create a duplicate `homework.md`. If an extra homework file already contains user answers, preserve it and create the next numbered extra homework file instead.
2. Use the current lesson summary as the main source.
3. Write every task heading, actionable instruction, purpose statement, label, note, and example explanation in Russian. Keep Dutch forms, answer options, dialogues, and other Dutch study material in Dutch. Starting with lesson 33, use the dedicated `om ... te` exercise described below instead of the English-to-Dutch translation section. If the user explicitly requests an English-to-Dutch exercise, keep its English source sentences in English, but write the heading and instructions in Russian. Do not add English explanations elsewhere.
4. Prioritize the grammar from the current lesson.
5. For the extra homework, draw on the whole cumulative `WORDS.md`, not only the current lesson. Every extra task should mix current-lesson grammar and vocabulary with words from earlier lessons so the user keeps revising. Do not build the extra tasks exclusively from current-lesson words.
6. Generate a substantial extra homework set by default. Use `les-06/homework.md` as the baseline size, then make `homework_extra.md` about twice as large unless the user asks for a shorter set.
7. Always use the same set of task types as `les-10/homework_extra2.md`, in this order:
   - fill-in-the-blank grammar for the current lesson's main grammar,
   - choose and fill in the comparative or superlative form (`comparatief` / `superlatief`),
   - `de`-woord or `het`-woord recognition,
   - Russian-to-Dutch translation,
   - before lesson 33: English-to-Dutch translation; starting with lesson 33: dedicated mixed grammar practice with `om ... te`,
   - ontkennende zinnen (`niet` / `geen`),
   - vragen (yes/no questions plus questions with a question word),
   - grammar terminology and exercise-instruction vocabulary from the screenshots,
   - listening dictation following the requirements below,
   - an answer key for every section.
   Add or adapt a grammar fill-in section to match the current lesson's grammar, but keep the overall structure above.
   Never generate tasks that cannot have a fixed answer key (e.g. `Spreken`, `Vertellen`, free writing / describe-a-picture prompts). Every task must have answers in the answer key.
8. Always include a Russian-to-Dutch translation section. Starting with lesson 33, replace the standard English-to-Dutch section with the dedicated `om ... te` exercise; include English-to-Dutch only when the user explicitly requests it.
9. If an English-to-Dutch section is explicitly requested, it and the Russian-to-Dutch section must use different sentences. Never reuse the same sentences or straight translations across the two sections.
10. Make translation sections large enough to be useful: usually 10–15 sentences. The dedicated `om ... te` exercise follows the standard 15–20-item size.
11. Keep the level appropriate for A0/A1 beginners.
12. Use simple sentences and familiar vocabulary.
13. Prefer sentences that combine the current lesson grammar with older vocabulary from `WORDS.md`.
14. If a screenshot already contains Russian prompts, preserve that style. Do not add English prompts unless the user explicitly requests a dedicated English-to-Dutch translation exercise.

### User's Standard Homework Requirements

Apply these requirements to generated extra homework unless the user explicitly asks for a different format:

1. Include exercises covering:
   - comparative and superlative forms, with context determining which form is required,
   - direct, indirect, and possessive pronouns: use 15 items, with exactly 10 practising full forms `hen` / `hun`, including direct objects, indirect objects without a preposition, `hen` after prepositions, and possessive `hun`; use the other 5 for other pronouns,
   - a dedicated reflexive-pronoun exercise (`me`, `je`, `zich`, `ons`), starting with lesson 22 and in all future homework sets; cover different subjects, questions, inversion, and known modal verbs,
   - negative sentences,
   - questions,
   - large numbers written in words, including ordinal numbers; starting with lesson 35, always include calendar dates, years, and clock times (both conversational and timetable readings), continuing the format introduced in lesson 34,
   - sentence building with conjunctions learned so far,
   - sentence building with modal verbs learned so far, always including `zullen` (for example a promise or a suggestion); starting with lesson 35, always include several items with `hoeven niet te` / `geen ... te`, including inversion and a separable verb, and distinguish lack of necessity from prohibition (`niet mogen`),
   - every new word or phrase added for the current lesson.
2. Write the source text for all the exercise types listed above in Russian so the user practises translating into Dutch.
3. Where meaningful, include plural nouns and a mixture of `de`-words and `het`-words in those exercises.
4. Give each standard exercise 15-20 sentences/items. The current-lesson vocabulary exercise may contain as many items as needed to cover every new word and phrase.
5. Keep the Russian-to-Dutch translation and dedicated `om ... te` practice as separate sections starting with lesson 33. For earlier lessons, or when explicitly requested, keep Russian-to-Dutch and English-to-Dutch as separate sections.
6. Keep the dedicated plural and `de`/`het` exercises.
7. Include one dedicated exercise that collectively covers all current-lesson vocabulary, and repeat every word and phrase at least once in another exercise in the same homework set.
   - Establish the full target list from the lesson source, summary, and relevant `WORDS.md` entries, including previously known vocabulary practised in the current lesson; do not limit coverage to newly added dictionary rows.
   - Distribute the additional occurrences naturally across the other exercises, using different sentences and contexts. Each word or phrase must be part of an actual learner task in both the dedicated vocabulary exercise and at least one other exercise. Mentions only in headings, instructions, hints, word lists, or answer keys do not count; inflected forms count when they practise the intended meaning.
   - Before delivery, check an internal coverage map from each target word or phrase to its numbered items in the dedicated exercise and in another exercise. Fill any gaps while preserving the required exercise types, sizes, and learned-material boundaries. Keep this map as a generation check only: do not publish it in the homework, answer key, or lesson summary. Apply this to newly generated homework; do not rewrite existing sets unless requested.
8. Provide a fixed answer key for every item; do not use open-ended tasks.
   - In answer keys involving possessive pronouns, include both full (stressed) and reduced (unstressed) forms wherever both are grammatically and contextually valid, for example `jouw/je`, `mijn/m’n`, and `zijn/z’n`. Show both variants in the answer; if emphasis or contrast requires the full form, give only that form. Do not invent a second form where none exists.
9. In conjunction and modal-verb exercises, do not name the required conjunction or modal verb beside each sentence, except for the explicit `want` / `omdat` rule below. The user should otherwise choose it independently. The answer key may show one natural solution even when other correct variants are possible. Starting with lesson 34, every conjunction exercise must contain at least one item whose primary answer uses `want`; do not include `want` only as an optional alternative. Starting with lesson 35, for every Russian «потому что» prompt in the conjunction exercise, explicitly specify `Подсказка: используйте want.` or `Подсказка: используйте omdat.` Include both conjunctions as primary answers in the exercise and match the key to each hint.
10. Before lesson 33, do not use `om ... te` infinitive constructions in generated homework or answer keys. Starting with lesson 33, include a dedicated 15–20-item `om ... te` exercise in every new homework set instead of the standard English-to-Dutch section. Mix statements, yes/no questions and question-word questions; present, imperfectum, perfectum and future contexts where natural; negation in the main clause and inside the `om ... te` clause; purpose and evaluation of an action (`Het is leuk om ...`, `Ik vind het leuk om ...`); and separable verbs (`op te staan`). Practise these alongside familiar modal verbs without `te`. The `hoeven niet te` / `geen ... te` construction introduced in lesson 34 is also allowed and must recur in the modal-verb exercise from lesson 35 onward. Other `te`-infinitive constructions and advanced infinitive combinations remain outside the taught material until separately introduced. Present this as regular cumulative grammar practice, not as a one-off response to a user request. Do not rewrite earlier homework solely to add this grammar.
11. Include a dedicated grammar-terminology exercise in every generated homework set. Test Dutch terms and common exercise instructions actually visible in the lesson screenshots, reusing terms from earlier lessons for revision. Examples, when present in the source, include `het meervoud` (множественное число), `het werkwoord` (глагол), and `kies de juiste optie` (выберите правильный вариант). Use Russian prompts asking the learner to supply or match the Dutch term or instruction, and provide a fixed answer key. Follow the standard 15–20-item size when enough source vocabulary is available; otherwise use fewer items rather than inventing terms supposedly seen in the screenshots. Add newly encountered terms and instruction phrases to `WORDS.md` with their Russian meanings and lesson id.
12. Starting with lesson 29, occasionally include a destination question with `naartoe` in the questions exercise, rotating it into future homework sets. Use a natural Russian prompt, such as «Куда ты едешь?», and a matching answer such as `Waar ga je naartoe?`. Keep the choice of Dutch wording independent: do not reveal `naartoe` in the prompt.
13. Include a listening dictation of 15–20 sentences in every newly generated extra homework set, in addition to the other exercises. The dictation is an exception to the Russian-source-text rule: the learner transcribes Dutch audio rather than translating a written prompt.

14. The learner has covered `dus` only as a coordinating conjunction. Use subject–finite verb order after `dus` in generated examples, exercises, answer keys, and dictation: `Ik ben moe, dus ik blijf thuis.` Do not use connective-adverb inversion (`dus blijf ik`) until the user says it has been covered. This does not change inversion after initial adverbials or initial subordinate clauses.

### Independent verb choice and learned constructions

- In reflexive-pronoun and strong/irregular-verb translation exercises, let the learner choose the verb independently. Do not append routine Dutch infinitive hints such as `(zich wassen)` or `Beginnen; perfectum`. Keep explicitly required hints from the rules below, such as `aanmelden` / `inschrijven`, unfamiliar vocabulary and necessary ambiguity clarification; do not turn these exceptions into hints for every item. Tense labels may remain.
- The user confirmed during lesson 35 that `zijn + aan het + infinitive` has not been studied. Its appearance in a screenshot does not establish that it has been taught. Exclude it from generated practice, answer keys and dictation until the user says otherwise; use the familiar present tense where appropriate. A source note may mention that it remains unlearned.

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
- Example from lesson 28, exercise 5, sentence 1: «Вчера я заблудился в Амстердаме.» → `Gisteren ben ik in Amsterdam verdwaald.` Use this order in the answer key rather than `Ik ben gisteren in Amsterdam verdwaald.`
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
- Keep dedicated de/het and plural exercises; their instructions may specify the requested dictionary form without revealing the answer.
- Use correct articles in the answer key. Russian may allow multiple interpretations: the key gives one natural translation, and grammatically correct article alternatives supported by the source meaning are acceptable. Explain meaningful differences in the key when helpful, not as hints in the prompt.

## Style

- Be clear, practical, and beginner-friendly.
- Use Dutch examples with English or Russian support when helpful.
- Do not over-explain advanced grammar unless needed.
- Make exercises easy to print or copy into notes.
- Keep answer keys separated from exercises.
