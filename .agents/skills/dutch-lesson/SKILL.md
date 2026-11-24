---
name: dutch-lesson
description: Generate Dutch lesson summaries, cumulative vocabulary, homework, and answer keys in the MuchDutch project from lesson screenshots, Miro materials, or notes. Also use for requests for homework for an existing lesson. Excludes checking the learner's answers and isolated grammar or translation questions.
---

# Dutch Lesson

Create lesson materials in the MuchDutch repository and review the generated content before delivery. Explain the material in Russian and keep Dutch study text in Dutch.

## Run two agents

For each new lesson or homework set, the coordinating assistant dispatches two distinct subagents via the collaboration tools. The coordinator owns the handoff and delivers the result. An agent assigned one of the roles below performs only that role and reports back to the coordinator.

1. Spawn the **generator** with the user’s request, source materials, project path, and requested scope. Give it the generation instructions below and sole responsibility for writing the lesson files. Wait for its handoff listing the exact files, any intentionally limited scope, and any unreadable source.
2. Once the draft is saved, spawn a fresh **reviewer**. Pass the original request, source materials, paths to the saved files, and the review instructions below. Keep the generator’s proposed answers and reasoning out of the handoff. The reviewer reads the learner-facing files first and opens the answer key only after solving the exercises. For attachments that cannot be passed as paths, supply the original input context. The reviewer reports findings to the coordinator and makes no file changes.
3. For each finding, send the section and item number, the mismatch, and the required correction back to the same generator. After corrections are saved, have the same reviewer reread the changed items, their answers, and any dependent counts, links or recordings. Deliver after the reviewer confirms the final files have no outstanding findings within scope. If independent review cannot run or a finding remains unresolved, report exactly what is unverified.

## Locate the project and load its requirements

- Work in the user's MuchDutch project, identified by `CODEX.md`, `WORDS.md`, and `les-XX` folders. If the current workspace is different, use an already supplied project path or ask for its location; do not create a second course repository.
- Read the project's `CODEX.md` before generating content. It is the single source of truth for file locations, the summary template, vocabulary normalization, exercise types and sizes, and translation preferences. Read the normalization rules at the top of `WORDS.md` as well. Do not copy these evolving rules into this skill.
- Determine the lesson number from the user's request and source. If they conflict or the number is missing and cannot be inferred reliably, ask before choosing a lesson folder.
- For an existing lesson, read its summary and homework before editing. Preserve user answers and notes. If a new homework set is needed, use the next available numbered homework file rather than replacing completed work.

## Generator — write the requested materials

1. Establish the scope. For new lesson screenshots or supplied lesson material, produce the summary, vocabulary updates, and homework with answers in one task, unless the user narrows the request. For an homework-only request, use the existing lesson summary; do not rewrite it or invent a new lesson.
2. Use the “Screenshot Analysis Workflow” in `CODEX.md` to select the source sections to analyze. Apply the screenshot-heading rule in `CODEX.md`: extract only new words and expressions from blocks labelled as homework. Record unreadable or uncertain content explicitly rather than inventing it.
3. Create or update `les-XX/README.md` using the template in `CODEX.md`. Distinguish the taught material from generated examples. Retain existing useful notes and link the generated practice file.
4. Update `WORDS.md` for new words, reusable phrases, and grammar or instruction vocabulary actually encountered. Search the entire file for matching meanings and functions before adding rows. Preserve existing meanings, notes, and lesson references. Identify the current lesson's new vocabulary from the source and the actual additions or new meanings, not from a section heading alone.
5. Build a homework coverage plan from `CODEX.md`: required sections, item counts, current grammar, new-vocabulary coverage, and earlier vocabulary for revision. Use its “Homework format” section for the section order, sizes and vocabulary coverage.
6. Generate the exercises and a separate answer key. Use the current lesson's grammar and previously learned constructions, with the source and earlier summaries establishing what has been covered. Draw revision words from across the cumulative vocabulary learned up to this lesson; avoid using later lessons as prerequisites when generating practice for an earlier lesson.
7. Apply the unfamiliar-vocabulary and tense-instruction rules in `CODEX.md` to every relevant written section. Check what the learner can infer before seeing the key.
8. Apply every Russian-to-Dutch translation preference in `CODEX.md` to all relevant sections, including initial adverbials and inversion, independent article choice, and valid possessive variants. Preserve the user's boundary that existing exercises and keys are not retroactively rewritten solely for the initial-adverbial rule.

## Reviewer — verify the saved materials independently

Read the project requirements, the source, and the draft on disk. For each written item, use only the visible instructions and prompt to determine the expected answer, permissible variants, and tense where relevant. Then open the key and compare. Return actionable findings by file, section and item, or confirm what you verified.

- **Coverage:** Check the required exercise types, section order, item counts, level, and mixture of current and earlier vocabulary against `CODEX.md`. Verify both numbered occurrences required by the vocabulary coverage rule, including previously known targets practised in the source. Check that screenshot homework headings contributed vocabulary only. Check that grammar terms are grounded in supplied materials or earlier documented lessons.
- **Unfamiliar vocabulary:** Verify each prompt, answer and dictation glossary against the evidence and per-item hint requirements in the “Unfamiliar vocabulary” section of `CODEX.md`.
- **Answer completeness:** Match every exercise item and sub-item to its answer using section and item numbers. Check for omissions, extra answers, broken numbering, and blanks left in the key. Fixed answer keys may include valid alternatives; they do not require every translation to have only one possible formulation.
- **Tense instructions:** For each finite form the learner supplies, check whether the prompt and section instructions satisfy the tense rules in `CODEX.md`. Flag missing or conflicting guidance even when the keyed sentence is grammatically correct. In mixed sections check that item ranges and clause-specific instructions match the actual answers.
- **Language correctness:** Check intended meaning, verb forms and auxiliary choice, tense, articles, plurals, adjective endings, pronouns, negation, questions, and main- and subordinate-clause word order. Pay particular attention to inversion after an initial adverbial. Flag items that need simplifying to stay within the taught material.
- **Hints for `er`:** Apply the `CODEX.md` section “Hints for `er` in translation exercises”: flag expected `er` and its role in new prompts, distinguish it from impersonal `het`, and accept contextually valid alternatives. Do not retrofit existing examples unless requested.
- **Prompt quality:** Check that Russian prompts are natural, required choices have enough context, and prompts do not leak article, conjunction, or modal-verb answers where independent choice is required. Check that Russian and English translation sections use distinct sentences, including their meanings.
- **Course boundaries:** Verify that the constructions used have been taught by the target lesson, applying the learned-construction rules in `CODEX.md`. Where both stressed and unstressed possessive forms are valid, include both as required by the project instructions.
- **Presentation:** Check Russian headings, explanations, labels, and instructions; allow English source sentences only when an English-to-Dutch section was explicitly requested, while preserving the dictionary's existing English columns. Keep internal generation artifacts such as vocabulary coverage maps out of the homework, answer key, and lesson summary. Keep Dutch learning text in Dutch. Verify links, readable Markdown tables, and any stated item totals.
- **Preservation:** Inspect the final changes to confirm that user responses, historical homework, unrelated lessons, and existing vocabulary information have been preserved. New requirements do not authorize a course-wide rewrite.

If the source remains partly unreadable, document the specific uncertainty and complete the supported material. Do not claim that uncertain forms or missing source content were verified.

## Coordinator — deliver

Give a short Russian response linking the summary, vocabulary, and homework files that were created or updated. State the main topic and any unresolved source uncertainty. Do not paste the full lesson into chat when it is already saved in files, or claim to have checked the learner's answers.
