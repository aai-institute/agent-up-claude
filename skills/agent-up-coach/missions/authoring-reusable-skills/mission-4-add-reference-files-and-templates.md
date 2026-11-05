---
id: mission-4-add-reference-files-and-templates
number: 4
title: Add reference files and templates
summary: Move the lists and templates you paste in every time into your skill's folder, so it stays short and fills the same layout every time. You leave with a skill folder v4.
artefact: "Skill v4: skill folder with a reference file and a template"
---

Track: Baseline
Level: practitioner
Time: 30 minutes
Tools: Claude chat, Cowork or Claude Code
Artefact kind: text
Artefact file: my-skill-v4.md

## Context
You still paste the same **list** or fix the same **layout** every time you use your skill, and putting it all into SKILL.md would make the skill long and harder to follow. A **reference file** and a **template** in the skill folder do this for you and keep the skill short.

## Your task
Move one block of **reference material** into a **[[reference file]]** with a **pointer**, add one **template** (an **[[asset]]**) your skill fills, and delete lines that **change nothing**.

## After this, you can
Decide for any material whether it belongs in SKILL.md, in references/ or in assets/, and point to it so it loads only when needed.

## You need
- Your **SKILL.md**, tested at least once, or the **working example** in this mission
- One block of **reference material** you paste in again and again (a list of categories, style rules, product names) and one **template** your output follows
- **Claude** with skills switched on

## You need [claude-code]
- Your **SKILL.md**, tested at least once, or the **working example** in this mission
- One block of **reference material** you paste in again and again (a list of categories, style rules, product names) and one **template** your output follows
- Your skill folder in **~/.claude/skills/[name]/**

## You need [chatgpt, gemini]
- Your **SKILL.md**, tested at least once, or the **working example** in this mission
- One block of **reference material** you paste in again and again (a list of categories, style rules, product names) and one **template** your output follows
- Your skill **installed** in your tool

## You need [no-skills]
- Your **SKILL.md**, tested at least once, or the **working example** in this mission
- One block of **reference material** you paste in again and again (a list of categories, style rules, product names) and one **template** your output follows
- Your **project** or **Gem**, which can hold **files** next to its instructions

## You should already
- Be able to **install a skill** and run a test in a **fresh chat**

## Concept
Heading: The 3 parts of a skill folder
Lead: A skill is a **folder**. SKILL.md holds what **every** request needs; the other folders hold what is needed **sometimes** or **in the result**.
- SKILL.md: The header and the **steps**. The AI reads it **every time** the skill runs, so it stays short.
- references/: **Knowledge** the AI opens only when a step points to it: rules, lists, definitions.
- assets/: **Files used in the result**, not followed as instructions: a template to fill, a logo, a sample layout.
Close: A **[[pointer]]** with a condition decides when a file is opened (**[[progressive disclosure]]**).
Toggle: Why not one long skill? | Everything in SKILL.md is read on **every** run, together with your request and your files. A long list that only some requests need makes the important steps easier to miss; Anthropic asks for **short, focused** skills (under **500 lines**).
Toggle: What else does a separate file give me? | You update a list **in one place** without touching the steps, and you can see at a glance what the skill knows and what it does.
Toggle: Is there a fourth folder? | Yes: **scripts/**, for steps that must be calculated exactly the same way every time. It is not needed for this mission.

## Check your understanding
Question: Your skill writes a monthly report. Every report must follow the same Word-style layout, and only reports for the board need the list of 40 risk categories. Where does each go?
- A: Both into SKILL.md, so nothing is missed
- B: The layout into assets/, the risk list into references/ with a pointer for board reports
- C: The layout into references/, the risk list into assets/
- D: Both into references/, without a pointer
Answer: B
Why: The layout is used in every output, so it is an asset the steps fill. The risk list is knowledge needed only for board reports, so it sits in references/ and a pointer with a condition opens it only then. A loads everything every time; D means the files are never or always read.

## Working example
Situation: Your **status update skill** writes a weekly update. You paste the **risk categories** for board versions, and you fix the **layout** by hand each time.
Input: Your **tested skill** (about 25 lines), the list of risk categories and the update layout.
- Move the categories into **references/risk-categories.md** with a pointer for board updates.
- Save the layout as **assets/update-template.md** and add a step to fill it.
- Delete one line that **changes nothing**.
Result: A **skill folder v4** that stays short, fills the same layout every time and reads the categories only when needed.
Ask: Do you want to work on a skill of your own, or the working example? Tell me what you paste in or fix by hand each time you use it.

## Steps
### Reference
Use: Work on a skill you wrote, or on the working example below.
Why: Knowledge that only **some** requests need does not belong in the always-loaded steps, and a file nobody points to is **never read**.
Do: Paste a list you **already have** (max 10 lines) into the chat as your reference file, give it a name, and add one **pointer** to your steps that names the file and says **when** to read it. Claude puts it into **references/** when it builds your ZIP.
Ask: Send the file name, what is in it, and your pointer line.
Code:
```text
File: references/[name].md
Pointer: [n]. If [condition], read references/[name].md before you answer.
```
Example:
```text
File: references/refund-rules.md (the 5 refund cases with their limits)
Pointer: 3. If the complaint mentions a refund, read references/refund-rules.md before you answer.
```
Weak:
```text
Moved all the steps into references/steps.md. Pointer: See the references folder for more information.
```

### Reference [no-skills]
Use: Work on a skill you wrote, or on the working example below.
Why: Knowledge that only **some** requests need does not belong in the instructions, and a file nobody points to is **never used** on purpose.
Do: Save one block of reference material as a **separate file**, add it to your **project** or **Gem**, and add one **pointer** to your instructions that names the file and says **when** to use it.
Ask: Send the file name, what is in it, and your pointer line.
Example:
```text
File: refund-rules.md (the 5 refund cases with their limits)
Pointer: 3. If the complaint mentions a refund, use refund-rules.md before you answer.
```
Weak:
```text
Uploaded all my instructions as a file, so the instructions field is empty.
```

### Template
Why: A template the AI **fills** gives the same layout every time, instead of a layout it rebuilds from a description.
Do: Paste a result you **already have** (max 8 lines), replace the parts that change with **[placeholders]**, name it **assets/[template-name].md**, and add one step that tells the AI to **fill that template**.
Ask: Send your template and the step that uses it.
Code:
```text
assets/[name].md:
[paste a result you already have, with [placeholders] for the parts that change]

Step: [n]. Fill assets/[name].md. Keep its order; replace only the [placeholders].
```
Example:
```text
assets/reply-template.md:
Subject: [short problem]
Dear [name], [apology for the problem]. [fix and date]. [contact line]

Step: 4. Fill assets/reply-template.md. Keep its order and headings; replace only the [placeholders].
```
Weak:
```text
Step: 4. Make it look like our usual replies.
```

### Template [no-skills]
Why: A template the AI **fills** gives the same layout every time, instead of a layout it rebuilds from a description.
Do: Save the layout your output always follows as a **template file** with **[placeholders]**, add it to your project or Gem, and add one instruction that tells the AI to **fill that template**.
Ask: Send your template and the instruction that uses it.
Code:
```text
[name].md:
[paste a result you already have, with [placeholders] for the parts that change]

Instruction: [n]. Fill [name].md. Keep its order; replace only the [placeholders].
```
Example:
```text
reply-template.md:
Subject: [short problem]
Dear [name], [apology for the problem]. [fix and date]. [contact line]

Instruction: 4. Fill reply-template.md. Keep its order and headings; replace only the [placeholders].
```
Weak:
```text
Instruction: 4. Make it look like our usual replies.
```

### Prune [standard, fast-track]
Why: Every line in SKILL.md is read on every run, so lines that change nothing only make the important ones easier to miss; once the template and the list do their job, some old lines are no longer needed. Using **one name** for your main idea everywhere (a **[[leading word]]**) stops the AI from treating two names as two different things.
Do: Remove **one line at a time** that you doubt and run the test that can show its effect: if the output stays the same, **delete it**. This is the **[[deletion test]]**. Use your **leading word** the same way in the description, the steps and the template.
Ask: Send the lines you deleted and your leading word; your full **skill v4** appears on the page.
Example:
```text
Deleted: "Use a clear structure" (the template does this now), "Always be polite" (stated twice).
Kept: "If the order number is missing, ask for it" (the output invented one without it).
Leading word: "fix-first reply", in the description, step 1 and the template title.
```
Weak:
```text
Everything is important, so I kept all of it.
```

### Go further [fast-track]
Why: An agent that sees a **long process** at once tends to rush the early steps to reach the end; splitting it into **phases** keeps each step thorough.
Do: Split your steps into **two phases** (for example "collect" and "write"), with a check between them, and add a short **table of contents** to any reference file longer than 100 lines.
Ask: Send your two phases and the check between them.

## Trust check
Watch for:
- Keep **real client data** out of references and assets; use **[placeholders]** in templates. (GDPR, Article 5)
- Check that a reference file does not **contradict** a [VERIFY] flag or an "ask, never guess" rule. (EU AI Act, Article 4)
- If you add a file you did not write (a template from the web, a logo pack), **read or open it** before you upload it. (Anthropic skill security)
Rules:
- GDPR, Article 5: Personal data must be adequate, relevant and limited to what is necessary for the purpose it is used for. [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- EU AI Act, Article 4: Organisations that provide or use AI systems must make sure their staff have enough AI literacy for their role: they understand the tools and what the outputs mean. [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- Anthropic skill security: Only use skills and files you created or got from a trusted source, and check every file first, because a skill can run code and fetch web content. [Anthropic docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
Ask: What in your reference file or template could be **out of date** in three months, and how will you notice?

## Test
Do: Ask Claude in a chat to build the **new ZIP** with your folders, upload it and switch the old version **off**; then send one request that **needs the reference file** in a **fresh chat**, and one that does **not** in **another fresh chat**.
Check:
- Claude reads the reference file **only** for the request that needs it.
- Both outputs follow your **template** exactly.
- SKILL.md is **no longer** than before, or longer only by the new step lines.
Ask: Did Claude open the reference file only when it was needed, and fill the template both times? Tell me what you expected and what came out.

## Test [claude-code]
Do: Save **references/** and **assets/** in your skill folder, start a **new session**, send one request that **needs the reference file**, and in another new session one that does **not**.
Check:
- The tool calls show the reference file is read **only** for the request that needs it.
- Both outputs follow your **template** exactly.
- SKILL.md is **no longer** than before, or longer only by the new step lines.
Ask: Did Claude Code read the reference file only when it was needed, and fill the template both times? Tell me what you expected and what came out.

## Test [gemini]
Do: Upload the **whole skill again** with its folders, then send one request that **needs the reference file** in a **new chat**, and one that does **not** in **another new chat**.
Check:
- Only the first answer uses details that are **only in the reference file**.
- Both outputs follow your **template** exactly.
- SKILL.md is **no longer** than before, or longer only by the new step lines.
Ask: Did only the right request use the reference file, and was the template filled both times? Tell me what you expected and what came out.

## Test [no-skills]
Do: Update the **instructions** with your pointer and template step, then send one request that **needs the file** and one that does **not**, each in a **new chat** in your project or Gem.
Check:
- The first answer uses details that are **only in the file**.
- Both outputs follow your **template** exactly.
- Your instructions are **no longer** than before, or longer only by the new lines.
Ask: Did the right request use the file, and was the template filled both times? Tell me what you expected and what came out.

## Other ways
- Cowork: Ask Cowork to **create references/ and assets/** in your skill folder from your text, then build the ZIP for you.
- skill-creator: Ask Claude to **use the skill-creator** to review your folder and suggest what to move out of SKILL.md.
- Activity: In a chat, open the **activity view** to see when your skill opens a file.

## Other ways [claude-code]
- Long references: Start any reference file over **100 lines** with a short table of contents, so the AI finds the right part.
- Project skill: Move the folder to **.claude/skills/** in one repository, so the skill and its files load only in that project.
- Binary assets: Put logos or sample spreadsheets in **assets/** and name them in the step that uses them.

## Other ways [chatgpt]
- Codex: Keep the same folder in **~/.agents/skills/**; Codex reads references and assets the same way.
- Editor: Open the Skills editor to add files **without a new upload**.
- Claude: The same folder works in Claude apps and Claude Code without changes.

## Other ways [gemini]
- Gemini CLI: Keep the same folder in **~/.gemini/skills/**; the CLI asks before it loads a skill.
- File types: The Gemini app accepts text, code, data, PDF and image files in a skill, up to **100 MB** in total.
- Claude: The same folder works in Claude apps and Claude Code without changes.

## Other ways [no-skills]
- Knowledge files: Keep each reference and template as **its own file** in the project or Gem, named so the pointer can find it.
- Skill-ready: Keep the folder shape (SKILL.md, references/, assets/) on your computer, so it uploads as a skill as soon as your tool has skills.
- Claude: The same folder uploads as a skill in Claude on any plan, including Free.

## Done when
- SKILL.md holds the steps, one pointer with a condition and one template step.
- references/ and assets/ hold one file each, with no real client data.
- Claude read the reference file only for the request that needed it, and filled the template both times.

## Practice
- Add a version line at the end of SKILL.md: "Version 3, [month year]".
- Find one more piece of knowledge in SKILL.md that only some requests need, and move it into references/.
- Run the deletion test on one more paragraph next week, after a few real uses.

## Reusable template
Name: Skill folder with references and assets
```text
[skill-name]/
  SKILL.md
  references/
    [reference-name].md
  assets/
    [template-name].md

SKILL.md:
---
name: [skill-name]
description: [Does what, using your leading word] for [whom]. Use when [words a user would say]. Do not use for [the near miss].
---
[Skill title]

Steps
1. [action, using your leading word: "[leading word]"]
2. If [condition], read references/[reference-name].md before you answer.
3. Fill assets/[template-name].md. Keep its order; replace only the [placeholders].

If [detail] is missing, ask for it. Never guess.
[VERIFY] [what a person must check]

Version [n], [month year].
```

## Glossary
- Progressive disclosure: Loading a skill in levels: the description always, the steps when it runs, the files only when a step asks for them.
- Reference file: A file in a skill's references/ folder with knowledge such as rules or lists, read only when a step needs it.
- Asset: A file in a skill's assets/ folder that is used in the output, such as a template to fill or a logo, not followed as instructions.
- Pointer: A line in a skill's steps that names a file and says when to read or use it.
- Leading word: A short term for a key idea, used the same way everywhere in a skill, so the AI repeats it and follows it.
- Deletion test: Removing one line from a skill and running the same test: if nothing changes, the line can go.

## Sources
- [Agent Skills specification](https://agentskills.io/specification): The folder layout (SKILL.md, references/, scripts/, assets/) and what each folder is for.
- [Anthropic: Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview): The three loading levels (description, steps, files), and the advice to use only files from trusted sources.
- [Anthropic: Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices): The 500-line limit, files one level deep, and a table of contents for reference files over 100 lines.
- [Anthropic engineering: Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills): Why a skill can hold far more material than fits in the context window.
- [Matt Pocock: Building Great Agent Skills (AI Engineer)](https://www.youtube.com/watch?v=UNzCG3lw6O0): Steps versus reference, context pointers, leading words such as "vertical slice", and the deletion test.
- [Google: Skills in the Gemini app](https://support.google.com/gemini/answer/17094296): Which file types a skill folder may hold in the Gemini app, and the 100 MB limit.

## Coach notes
Arc: fourth of five in this topic (write the skill; install it and add an example; test and fix; reference files and templates; connect and get ready to share). Never name the other missions by number to the learner. Levels covered: structure (folder anatomy, references, templates, pointer, leading word, pruning).
Levels: guided (A, B) works on the working example or moves one list and one template, sees each example first, and hears plain words ("template" rather than "asset" until the learner uses it); standard (C) chooses the material alone; fast-track (D) gets the Go further step (phases, table of contents) and may discuss scripts/.
Guided mode (default for beginners): before a beginner writes each part, point to the step's "See an example" on the page, say in one sentence why it works (for example: "the pointer names a condition"), then ask for their version for their own case. Some familiarity: they try first and you point to the example after the first try. Experienced: only when they ask. The example is from a different case, so they adapt it instead of copying it.
Reference versus asset: a reference is read to decide or check something (rules, categories, definitions); an asset is used in the output (template, logo, sample layout). If the learner is unsure, ask: "Does the AI need to know this, or to fill or attach it?"
Short skill: most tested skills are 20 to 40 lines. The material usually comes from what the learner pastes into the chat or fixes by hand each time, not from SKILL.md. Ask: "What do you paste in or fix every time you use this skill?" Material every request needs and that is short (a rule of three lines) can stay in SKILL.md. Never invent material for them.
Leading word and trigger: keep the words users type as trigger words in the description; the leading word names the output and the core idea.
Likely errors: steps moved into the reference file instead of knowledge; a pointer without a condition ("see references"); a reference file that points to another reference file (keep one level deep); a template without placeholders, so the AI copies it literally; a template step that says "use" instead of "fill and keep the order"; real client data in the template; the ZIP holds a folder inside a folder; v2 and v3 both switched on.
Conflicts: a reference file that renames or adds things can break an existing VERIFY or "never guess" rule. Ask the learner to reread their checks after the Reference step.
Checking the test: in Claude apps the activity view shows which files the skill opened; in Claude Code the tool calls show it. If the learner cannot see it, ask for an output that only the reference file could produce.
Cannot upload today: paste SKILL.md, the reference file and the template into a fresh chat and ask Claude to follow the skill; say plainly that this shows the content works but not that the file loads only when needed.
Time budget for guided learners (30 minutes in total, profile and level question included): about 4 to 5 minutes per build step. They copy the step's fill-in lines and fill the [blanks]; they never write a part from an empty page. If a step runs over 8 minutes, accept a short version and note one improvement for later. The list and the template come from material the learner already has; never ask them to type a new one.
Feedback: name what the move achieved (a clear condition, a filled layout, a line removed), then the gap, then one fix.
Page state: set the full skill v4, the reference file and the template as the part for the last step (Template for guided; Prune for standard; Go further for fast-track). Guided learners skip Prune and the leading word; mention them only if asked.
Other vendors: ChatGPT and Codex read the same folder from .agents/skills; the Gemini app accepts a ZIP with SKILL.md at its root (max 100 MB, no Word or Excel files inside); Gemini CLI uses ~/.gemini/skills/.
