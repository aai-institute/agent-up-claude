---
id: mission-1-write-your-first-skill
number: 1
title: Write your first skill
summary: Turn a task you explain to AI again and again into a skill it loads by itself. You leave with a complete SKILL.md with a trigger, instructions and checks.
artefact: "Skill v1: SKILL.md with trigger, instructions and checks"
---

Track: Baseline
Level: foundation
Time: 30 minutes
Tools: Claude chat, Cowork or Claude Code
Artefact kind: text
Artefact file: my-skill-v1.md

## Context
After every **team meeting** you tell your AI chat the **same rules** again: turn my notes into a follow-up email, list what we agreed, add the next steps with dates, keep it short. And the result still changes each time. With a **[[skill]]** you explain it **once**, and the AI gets it right **by itself** every time the task comes up. It saves you time every week, and writing one is easier than it looks.

## Your task
After this mission, you will be able to **create basic skills on your own**.

## After this, you can
In the next steps you see **what a skill is**, write **your first skill** step by step, and **test it** to see how it really works.

## You need
- **Claude** chat, Cowork or Claude Code, on any plan
- A **task you repeat** at least monthly, with a similar output each time, or the **working example** in this mission

## You need [claude-code]
- **Claude Code** in your terminal or editor
- A **task you repeat** at least monthly, with a similar output each time, or the **working example** in this mission

## You need [chatgpt]
- **ChatGPT** in a Business, Enterprise, Healthcare or Edu workspace with **skills** switched on, or **Codex**
- A **task you repeat** at least monthly, with a similar output each time, or the **working example** in this mission

## You need [gemini]
- The **Gemini app** with a personal Google account and **skills**, or **Gemini CLI**
- A **task you repeat** at least monthly, with a similar output each time, or the **working example** in this mission

## You need [no-skills]
- Your usual **AI chat** (for example ChatGPT, Gemini or Copilot) with a way to open a **new chat**
- A **task you repeat** at least monthly, with a similar output each time, or the **working example** in this mission

## You should already
- Be able to write a prompt with a **task, context and success criteria**

## Concept
Heading: The 3 parts every skill needs
Lead: A skill is a **file of instructions** that the AI reads **only when the task comes up**. For example, a skill that turns **your notes from the week** into a short summary. No coding needed: it is **plain text**.
- Name: What the skill does, in **lowercase with hyphens**. Example: **weekly-notes-summary**
- Description: The [[trigger]] that tells the AI **when** to use the skill, and when not (the **[[near miss]]**). Example: "Use when I paste my notes from the week. Not for meeting minutes."
- Instructions: The **steps** the AI follows, one by one. Example: "1. Group the notes by project. 2. Write what is done and what is next. 3. Keep it to half a page."
Toggle: Why a skill and not a saved prompt? | A prompt works only when you remember to paste it. The AI reads every skill's **name and description** all the time, just a few lines each, and opens the **instructions only when** a request matches.
Toggle: Is a skill only one file? | A skill is a **folder**. SKILL.md is the only file it needs to start; lists, templates and other files can be added to the folder later.

## Check your understanding
Question: You have three skills installed. Which part does the AI read to decide whether to use one of them for your request?
- A: The numbered steps in the instructions
- B: The name and description in the header
- C: The examples at the end of the file
- D: All three, every time
Answer: B
Why: Only the header, a few lines per skill, is always read. The instructions and examples load after the AI has chosen the skill from its description, so D would fill the context with every skill at once.

## Working example
Situation: After each **team meeting**, you turn your notes into a **follow-up email**.
Input: Your **meeting notes**, without client names.
- Write what the team **agreed**, in short points.
- List the **next steps**, each with a date.
- Ask for the **date** if a step has none, instead of guessing.
Result: A **skill** that writes the follow-up email the same way after every meeting.

## Steps
### Trigger
Use: Pick a task of your own, or use the working example below. The best tasks are ones you **repeat**, with a result of the **same shape** each time, where you know what **good** looks like.
Why: The description is the **only part** the AI reads before it decides, so a vague one means the skill never loads, and a broad one means it loads for the wrong requests.
Do: Write the **name** and a **[[description]]** of about 200 characters: what the skill does, **when** to use it, and **when not**.
Ask: Send your skill **[[header]]**, the name and description, in the chat.
Code:
```text
---
name: [what-it-does-with-hyphens]
description: [Does what] for [whom]. Use when [words someone would type]. Do not use for [a similar request that needs something else].
---
```
Example:
```text
---
name: complaint-reply-drafts
description: Drafts replies to customer complaints in our support tone, with an apology, the fix and a next step. Use when the user pastes a complaint email or asks for a complaint reply. Do not use for sales emails or internal messages.
---
```
Weak:
```text
---
name: My Email Helper
description: I help with emails.
---
```

### Instructions
Why: Each step must be a **concrete action**: "be professional" is vague, so the AI guesses, but "start with one sentence that names the problem" it does the same way every time.
Do: Write your **steps**, **one action** per step, and the **[[output format]]**.
Ask: Send them in the chat.
Code:
```text
# Steps
1. [first action]
2. [next action]
3. [next action]

# Output format
[length], [structure], [language]
```
Example:
```text
# Steps
1. Name the customer's problem in one sentence, in their words.
2. Apologise once, for that specific problem.
3. State the fix or the next step, with a date if the complaint gives one.
4. End with one contact line.

# Output format
Max 120 words. Plain text, no bullet points. Same language as the complaint.
```
Weak:
```text
Write a nice, professional reply that makes the customer happy.
```

### Checks
Why: When a detail is missing, the AI fills the gap with something that sounds right, so the result **looks correct while it is wrong**.
Do: Write **one rule** for when a detail is missing, and **one [[VERIFY flag]]** for what a person must check.
Ask: Send your two lines in the chat.
Code:
```text
# When something is missing
- If [detail] is missing, ask for it. Never guess.

# Check before you answer
- [VERIFY] [the figure, date or name that must match the input]
```
Example:
```text
# When something is missing
- If the order number is missing, ask for it. Never invent one.

# Check before you answer
- [VERIFY] Every refund amount or date appears in the complaint or in what the user said.
```
Weak:
```text
Be accurate and double-check everything.
```

### Go further [fast-track]
Why: When you have several skills, two descriptions can **compete** for the same request, and the AI may pick the wrong one.
Do: Write the header of a **second skill** close to yours (for example the internal version of the same task), so that each description names the other as its **near miss**.
Ask: Send both headers.
Example:
```text
complaint-reply-drafts: ... Do not use for internal escalation notes.
complaint-escalation-notes: Writes the internal note to the team lead about a complaint. Do not use for replies to the customer.
```

## Trust check
Watch for:
- Keep **real names and client details** out of the skill. It is saved, reused and may be shared later. (GDPR, Article 5)
- Put a **[VERIFY]** flag on every step where a wrong figure, date or name could reach someone. (EU AI Act, Article 4)
- If you test with a **real document**, remove **personal and confidential data** first, above all in a free AI tool. (GDPR, Article 5)
Rules:
- GDPR, Article 5: Personal data must be adequate, relevant and limited to what is necessary for the purpose it is used for. [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- EU AI Act, Article 4: Organisations that provide or use AI systems must make sure their staff have enough AI literacy for their role: they understand the tools and what the outputs mean. [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- Swiss FADP, Article 6: For learners in Switzerland, personal data must be processed lawfully, in good faith and in proportion to its purpose. [Fedlex](https://www.fedlex.admin.ch/eli/cc/2022/491/en)
Ask: Which step in your skill could produce something that **looks right but is wrong**?

## Test
Do:
1. Download your **SKILL.md** from the chat.
2. In Claude, open a **[[new chat|fresh chat]]** outside any project.
3. Turn on **incognito chat** (the ghost icon at the top right), so your memory does not shape the answer.
4. Attach your **SKILL.md** and write: **"Use this skill. Invent a short example of the document it handles, with no real data and one detail missing, and apply the skill to it."**
5. Prefer your own document? Write **"Use this skill on this document:"** and paste it below.
Check:
- The output follows your **instructions and format** without edits.
- Where the sample leaves something out, the AI **asks** instead of guessing.
- Someone reading only your description could say **when** it should run.
Ask: Did the output follow your skill? Tell me what you expected and what came out.

## Test [claude-code]
Do:
1. Save your skill as **~/.claude/skills/[name]/SKILL.md**.
2. Start **claude** in a folder without project files.
3. Ask it to do your task on **a short made-up example**, with no real data and one detail missing.
Check:
- Claude Code says it **uses your skill** for the sample.
- The output follows your **instructions and format** without edits.
- Where the sample leaves something out, the AI **asks** instead of guessing.
Ask: Did your skill load and did the output follow it? Tell me what you expected and what came out.

## Test [chatgpt]
Do:
1. Download your **SKILL.md** from the chat.
2. In ChatGPT, open a **[[new chat|fresh chat]]** outside any project.
3. Turn on **Temporary Chat** at the top, so your memory does not shape the answer.
4. Attach your **SKILL.md** and write: **"Use this skill. Invent a short example of the document it handles, with no real data and one detail missing, and apply the skill to it."**
5. Prefer your own document? Write **"Use this skill on this document:"** and paste it below.
Check:
- The output follows your **instructions and format** without edits.
- Where the sample leaves something out, the AI **asks** instead of guessing.
- Someone reading only your description could say **when** it should run.
Ask: Did the output follow your skill? Tell me what you expected and what came out.

## Test [gemini]
Do:
1. Download your **SKILL.md** from the chat.
2. In the Gemini app, open a **[[new chat|fresh chat]]**.
3. Turn on **Temporary chat**, so your past chats do not shape the answer.
4. Attach your **SKILL.md** and write: **"Use this skill. Invent a short example of the document it handles, with no real data and one detail missing, and apply the skill to it."**
5. Prefer your own document? Write **"Use this skill on this document:"** and paste it below.
Check:
- The output follows your **instructions and format** without edits.
- Where the sample leaves something out, the AI **asks** instead of guessing.
- Someone reading only your description could say **when** it should run.
Ask: Did the output follow your skill? Tell me what you expected and what came out.

## Test [no-skills]
Do:
1. Download your **SKILL.md** from the chat.
2. In your AI chat, open a **[[new chat|fresh chat]]** outside any project.
3. Use its **temporary or private chat** if it has one, so your memory does not shape the answer.
4. Attach your **SKILL.md** (or paste its text) and write: **"Use this skill. Invent a short example of the document it handles, with no real data and one detail missing, and apply the skill to it."**
5. Prefer your own document? Write **"Use this skill on this document:"** and paste it below.
Check:
- The output follows your **instructions and format** without edits.
- Where the sample leaves something out, the AI **asks** instead of guessing.
- Someone reading only your description could say **when** it should run.
Ask: Did the output follow your skill? Tell me what you expected and what came out.

## Other ways
- Cowork: Ask Cowork to **save your text** as SKILL.md in a skill folder in your connected folder, ready to install.
- skill-creator: Ask Claude to **use the skill-creator** to interview you and draft a skill, then check every line the way you did here.

## Other ways [claude-code]
- Call it by name: Type **/[name]** at the start of a message to run your skill on purpose, even when the description would not trigger it.
- skill-creator: Ask Claude Code to **use the skill-creator** to interview you and draft a skill, then check every line the way you did here.
- Claude app: Upload the same folder as a ZIP in **Customize > Skills** to use the skill in Claude chat and Cowork too.

## Other ways [chatgpt]
- Create with chat: In **Plugins > Skills**, choose **Create with chat** and let ChatGPT interview you, then check every line the way you did here.
- Codex: Save the folder in **~/.agents/skills/** and call it with **$[name]**.
- Claude: The same SKILL.md works in Claude apps and Claude Code without changes.

## Other ways [gemini]
- Create with Gemini: In **Settings > Skills**, choose **Create with Gemini**, then check every line the way you did here.
- Gemini CLI: Save the folder in **~/.gemini/skills/** and type **/skills list** to see it.
- Claude: The same SKILL.md works in Claude apps and Claude Code without changes.

## Other ways [no-skills]
- Project or Gem: Paste the instructions into **project instructions** (ChatGPT) or a **Gem** (Gemini). They apply to every chat there, so the description does not trigger anything.
- Prompt library: Save the SKILL.md as a file and paste it into a new chat when the task comes up.
- Later: When your tool or plan gets skills, the same SKILL.md works without changes.

## Done when
- Your SKILL.md has a name, a description with a near miss, numbered instructions and an output format.
- It has at least one "ask, never guess" rule and one [VERIFY] flag.
- Your test output needed no edits, or you know which part to fix next.

## Practice
- Write a second near miss and check that your description already excludes it.
- Add one more [VERIFY] flag to the step you trust least.
- Rewrite one instruction that describes a quality ("be clear") as an action ("one sentence per point").

## Reusable template
Name: Skill v1 template
```text
---
name: [what-it-does-in-lowercase-with-hyphens]
description: [Does what] for [whom]. Use when [words a user would say]. Do not use for [the near miss].
---

[Skill title]

# Steps
1. [first action]
2. [next action]
3. [next action]

# Output format
[length, structure, language]

# When something is missing
- If [detail] is missing, ask for it. Never guess.

# Check before you answer
- [VERIFY] [the figure, date or name that must match the input]
```

## Glossary
- Skill: A folder with a SKILL.md file of instructions that the AI loads only when a task needs it.
- Trigger: The match between a request and a skill's description that makes the AI load the skill.
- Description: The part of a skill's header that says what it does, when to use it and when not; the AI reads it to decide.
- Output format: The shape of the answer: length, structure, sections and language.
- VERIFY flag: A marker in a skill for a step whose output a person must check before it is used.
- Near miss: A request that looks similar to your task but needs something else, so the skill must not start.
- Header: The block between the two --- lines at the top of SKILL.md, with the name and description.
- Fresh chat: A new chat with no earlier messages and memory off, so only your skill and request shape the answer.

## Sources
- [Anthropic: Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview): The structure of a skill and why only the name and description, a few lines per skill, are always read.
- [Anthropic: Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices): How to write the description in the third person with what the skill does and when to use it.
- [Claude Help Centre: How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills): What goes into a SKILL.md, and why no passwords or keys belong in a skill.
- [Agent Skills specification](https://agentskills.io/specification): The open standard: name up to 64 characters, description up to 1,024, used by ChatGPT, Gemini CLI and others too.
- [Anthropic: The complete guide to building skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf): The 15 to 30 minute estimate for a first skill and the naming rules.
- [Matt Pocock: Building Great Agent Skills (AI Engineer)](https://www.youtube.com/watch?v=UNzCG3lw6O0): Why every automatic skill adds context, and why a clear trigger keeps it predictable.

## Coach notes
Arc: first of five in this topic (write the skill; install it and add an example; test and fix; reference files and templates; connect and get ready to share). Never name the other missions by number to the learner. Levels covered: spot a task, trigger, steps, a first guard. The learner leaves with the simplest skill that works.
Levels (from the topic's level question, see SKILL.md): guided (A, B) uses the working example or a simple own task, sees each step's example before writing, and hears plain words only; standard (C) tries first, then sees the example; fast-track (D) may test out by pasting an existing skill that meets Done when, and gets the Go further step (overlapping descriptions). Technical words (token, frontmatter, MCP) only for fast-track or once the learner uses them.
Guided mode (default for beginners): before a beginner writes each part, point to the step's "See an example" on the page, say in one sentence why it works (for example: "it names a near miss"), then ask for their version for their own case. Some familiarity: they try first and you point to the example after the first try. Experienced: only when they ask. The example is from a different case, so they adapt it instead of copying it; if they copy it word for word, ask what changes for their task. Beginners can also take the working example instead of their own task, so the page example and their task differ only in the details.
Own task (standard and fast-track only; skip for guided to save time): when the learner picks their own task, ask once which parts the AI should do and which stay with them (judgement, sign-off). Pilot learners asked for this task split before writing the skill. Keep it to one question.
Pilot feedback to respect: never ask the learner to guess what the page has just explained; never draft the whole skill before they write it (pilot learners lost motivation when asked to rewrite a skill Claude had already written); ask for short answers where possible.
Likely errors: the name has capitals or spaces; the description says what but not when, or has no near miss; the description is in the first person ("I help..."); instructions describe qualities ("be professional") instead of actions; no rule for missing information, so the skill guesses; a real email with client names pasted into the skill as an example.
People data (HR, candidates, health): only made-up or anonymised samples; the decision about a person stays with a person; company rules and, in Germany, the works council decide what may be pasted into an AI tool. The EU AI Act treats AI used to select or evaluate candidates as high-risk, so a skill like this only drafts and a person decides.
Feedback: name the part that works, then the one gap, then one fix. For the description, ask: "Which request would someone send that looks like this but is not this task?"
Real case for the near miss: a pilot learner's text-compression skill triggered on "summarise" and kept firing for summaries, a different task. Use it when a learner's trigger is too broad.
Description language: the sources do not say which language works best. If the learner works in two languages, suggest naming trigger words in both and checking it in the install-and-test mission; do not claim more.
Page state: set the full skill as the part for the last step (Checks; Go further for fast-track) when it is final, so the learner can copy it.
Claude Code: in the claude-code variant the test already saves the skill in ~/.claude/skills/ and tests the trigger, so the install step in the next mission becomes a quick check. Start the test in a new session in a folder without a CLAUDE.md, so nothing else shapes the result.
Skill or something else (experienced learners): a skill fits a repeated task with a fixed shape; a CLAUDE.md or project instructions fit rules that apply to every request; a plain script fits a step with no judgement at all.
Test: deliver the learner's SKILL.md as a downloadable draft file before the test (SKILL.md rule in SKILL.md §8). Attaching it tests the steps, not the automatic start; say so plainly. If the result shows something to refine, they change it in this chat and you deliver the updated file.
Time budget for guided learners (30 minutes in total, profile and level question included): about 4 to 5 minutes per build step. They copy the step's fill-in lines and fill the [blanks]; they never write a part from an empty page. If a step runs over 8 minutes, accept a short version and note one improvement for later.
Time: allow at most two feedback rounds per step; if a part is still weak, note it as something to fix later and move on. If the learner's own task is complex, keep the sample input for the test short (5 to 10 lines). If time runs out, the test can open the next session.
Other vendors: ChatGPT and Codex read the same SKILL.md (ChatGPT skills on eligible Business, Enterprise and Edu workspaces, called with @skill); the Gemini app is replacing Gems with skills (personal accounts from November 2026), called with "/". Where equivalence breaks: a Custom GPT's or Gem's instructions are always on and do not trigger, so the description has no effect there.
