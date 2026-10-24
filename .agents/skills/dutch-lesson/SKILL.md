---
name: dutch-lesson
description: Generate Dutch lesson summaries, cumulative vocabulary, extra homework, and answer keys in the MuchDutch project from lesson screenshots, Miro materials, or notes. Also use for requests for additional homework for an existing lesson. Excludes checking the learner's answers and isolated grammar or translation questions.
---

# Dutch Lesson

Create lesson materials in the MuchDutch repository and review the generated content before delivery. Explain the material in Russian and keep Dutch study text in Dutch.

## Locate the project and load its requirements

- Work in the user's MuchDutch project, identified by `CODEX.md`, `WORDS.md`, and `les-XX` folders. If the current workspace is different, use an already supplied project path or ask for its location; do not create a second course repository.
- Read the project's `CODEX.md` before generating content. It is the single source of truth for file locations, the summary template, vocabulary normalization, exercise types and sizes, and translation preferences. Read the normalization rules at the top of `WORDS.md` as well. Do not copy these evolving rules into this skill.
- Determine the lesson number from the user's request and source. If they conflict or the number is missing and cannot be inferred reliably, ask before choosing a lesson folder.
- For an existing lesson, read its summary and extra homework before editing. Preserve user answers and notes. If a new homework set is needed, use the next available numbered extra file rather than replacing completed work.

## Generate the requested materials

1. Establish the scope. For new lesson screenshots or supplied lesson material, produce the summary, vocabulary updates, and extra homework with answers in one task, unless the user narrows the request. For an additional-homework request, use the existing lesson summary; do not rewrite it or invent a new lesson.
2. Inspect the supplied source, including grammar, vocabulary, pronunciation, listening, speaking, and writing material where present. Identify source homework so it is not reproduced. Record unreadable or uncertain content explicitly rather than inventing it.
3. Create or update `les-XX/README.md` using the template in `CODEX.md`. Distinguish the taught material from generated examples. Retain existing useful notes and link the generated practice file. Do not fabricate listening or speaking activities absent from the source.
4. Update `WORDS.md` for new words, reusable phrases, and grammar or instruction vocabulary actually encountered. Search the entire file for matching meanings and functions before adding rows. Preserve existing meanings, notes, and lesson references. Identify the current lesson's new vocabulary from the source and the actual additions or new meanings, not from a section heading alone.
5. Build a homework coverage plan from `CODEX.md`: required sections, item counts, current grammar, new-vocabulary coverage, and earlier vocabulary for revision. Use its historical examples for scale and structure only; current requirements take precedence over outdated wording or task formats in those examples.
6. Generate the exercises and a separate answer key. Use the current lesson's grammar and previously learned constructions, with the source and earlier summaries establishing what has been covered. Draw revision words from across the cumulative vocabulary learned up to this lesson; avoid using later lessons as prerequisites when generating practice for an earlier lesson.
7. Apply every Russian-to-Dutch translation preference in `CODEX.md` to all relevant sections, including initial adverbials and inversion, independent article choice, and valid possessive variants. Preserve the user's boundary that existing exercises and keys are not retroactively rewritten solely for the initial-adverbial rule.

## Review the generated content

This review concerns the materials just generated, not grading the learner's answers. Read the final files and correct problems within the current scope before delivering them.

- **Coverage:** Check the required exercise types, section order, item counts, level, and mixture of current and earlier vocabulary against `CODEX.md`. Confirm that the dedicated current-vocabulary exercise collectively covers every newly introduced word or phrase. Check that grammar terms are grounded in supplied materials or earlier documented lessons.
- **Answer completeness:** Match every exercise item and sub-item to its answer using section and item numbers. Check for omissions, extra answers, broken numbering, and blanks left in the key. Fixed answer keys may include valid alternatives; they do not require every translation to have only one possible formulation.
- **Language correctness:** Independently solve the generated prompts and compare them to the key. Check intended meaning, verb forms and auxiliary choice, tense, articles, plurals, adjective endings, pronouns, negation, questions, and main- and subordinate-clause word order. Pay particular attention to inversion after an initial adverbial. If an item cannot be answered with the taught material, simplify it.
- **Prompt quality:** Check that Russian prompts are natural, required choices have enough context, and prompts do not leak article, conjunction, or modal-verb answers where independent choice is required. Check that Russian and English translation sections use distinct sentences, including their meanings.
- **Course boundaries:** Check restrictions such as unlearned `om ... te` and other unfamiliar infinitive constructions. Where both stressed and unstressed possessive forms are valid, include both as required by the project instructions.
- **Presentation:** Check Russian headings, explanations, labels, and instructions; allow English source sentences only in the dedicated English-to-Dutch section, while preserving the dictionary's existing English columns. Keep Dutch learning text in Dutch. Verify links, readable Markdown tables, and any stated item totals.
- **Preservation:** Inspect the final changes to confirm that user responses, historical homework, unrelated lessons, and existing vocabulary information have been preserved. New requirements do not authorize a course-wide rewrite.

If the source remains partly unreadable, document the specific uncertainty and complete the supported material. Do not claim that uncertain forms or missing source content were verified.

## Deliver

Give a short Russian response linking the summary, vocabulary, and homework files that were created or updated. State the main topic and any unresolved source uncertainty. Do not paste the full lesson into chat when it is already saved in files, or claim to have checked the learner's answers.
