---
id: mission-3-test-and-fix-your-skill
number: 3
title: Test your skill and fix what breaks
summary: Try your skill with three short test requests, including one it must ignore, and fix the one part behind each failure. You leave with a tested skill v3 you can rely on.
artefact: "Skill v3: tested and fixed SKILL.md"
---

Track: Baseline
Level: foundation
Time: 30 minutes
Tools: Claude chat, Cowork or Claude Code
Artefact kind: text
Artefact file: my-skill-v3.md

## Context
A skill that worked once can still fail on the next **unusual request**, and you often notice only when a colleague or client does. **Three short tests** and one fix per failure show you where it breaks first.

## Your task
Write **3 test requests** with the result you expect, run each in a fresh chat, and **fix** the one part behind each failure.

## After this, you can
Tell from a failed test which part of a skill caused it, and fix that part alone.

## You need
- Your **installed skill** with an example, or the **working example** in this mission
- **2 or 3 short sample inputs** (5 to 10 lines each), with names made up

## You need [no-skills]
- Your **skill** in a project or Gem, or the **working example** in this mission
- **2 or 3 short sample inputs** (5 to 10 lines each), with names made up

## You should already
- Be able to **install a skill** and run it in a **fresh chat**

## Concept
Heading: The 3 tests every skill needs
Lead: Each test is **one request** with the result you **expect**, written **before** you run it.
- Normal: Should **start** the skill, with typical input. Shows the skill does its job.
- Awkward: Should start it, with **missing or odd** input. Shows whether it asks or guesses.
- Near miss: Should **not start** it. Shows whether the description is too broad.
Close: This is the **full test** of your skill. Anthropic recommends **at least 3 tests**; keep samples to **5 to 10 lines** so testing stays quick.
Toggle: Where can a failure come from? | From **one part**: the description (the skill starts for the wrong request), the steps (wrong actions), the format (wrong shape) or a **[[missing rule]]** (invented details).
Toggle: Do I have to run all three tests after every change? | No. After a small change, check **only what you changed**. Run all three again when you want to **rely on** the skill for real work.

## Check your understanding
Question: Your test request is "Draft a sales email about our new offer" and your skill writes complaint replies. Which result counts as a pass?
- A: The skill starts and writes a polite sales email
- B: The skill does not start
- C: The skill starts and asks for an order number
Answer: B
Why: This is a near miss: it looks similar but is a different task, so the right result is that the skill stays quiet. A and C both mean the description is too broad.

## Working example
Situation: Your **status update skill** is installed. You want to know how it handles a **missing due date** and a request for **meeting minutes**.
Input: Your **installed skill** and three short sample notes, names made up.
- Write the **normal** test with complete notes.
- Write the **awkward** test with one task missing its due date.
- Write the **[[near miss]]**: a request for meeting minutes.
- Run each in a **fresh chat** and fix the **one part** behind each failure.
Result: A **skill v3** that passes all three tests.
Ask: Do you want to test a skill you wrote, or the working example? If you have no skill yet, say so and I will give you a short one to test.

## Steps
### Test set
Use: Work on a skill you wrote, or on the working example below.
Why: A test only counts when you wrote the **expected result before** the run; afterwards, any output can look right.
Do: Write **3 test requests**: normal, awkward and near miss, each with the **result you expect**. Ask in the chat for **made-up samples** for your task, so you do not have to type them.
Ask: Send your **[[test set]]** in the chat.
Code:
```text
1. Normal: "[request]" + [sample]  Expect: [what a good result contains]
2. Awkward: "[request]" + [sample with something missing]  Expect: asks for [...]
3. Near miss: "[similar request, different task]"  Expect: skill does not start
```
Example:
```text
1. Normal: "Draft a reply to this complaint about a late delivery." (order number included)
   Expect: skill loads, under 120 words, apology, delivery date.
2. Awkward: a complaint with no order number.
   Expect: skill loads, asks for the order number, invents nothing.
3. Near miss: "Draft a sales email about our new delivery plan."
   Expect: skill does not load.
```
Weak:
```text
Try it with a few emails and see if it works.
```

### Run
Why: A **fresh chat** for each test makes sure only your skill and the request shape the answer, not what you said before.
Do:
1. Open a **fresh chat** with memory off.
2. Send **test 1** with its sample and note whether Claude says it **uses your skill**.
3. Compare the output with what you **expected** and mark pass or fail.
4. Repeat for **test 2** and **test 3**, each in a new fresh chat.
Ask: Send your results: each test, pass or fail, and what came out where it failed.

### Run [claude-code]
Why: A **fresh session** for each test makes sure only your skill and the request shape the answer, not what you said before.
Do:
1. Start a **new session** (**claude**) in a folder without a CLAUDE.md, so project rules do not shape the test.
2. Send **test 1** with its sample and note whether Claude Code says it **uses your skill**.
3. Compare the output with what you **expected** and mark pass or fail.
4. Repeat for **test 2** and **test 3**, each in a new session. Run the near miss **3 times**: triggering can vary.
Ask: Send your results: each test, pass or fail, and what came out where it failed.

### Run [chatgpt, gemini]
Why: A **fresh chat** for each test makes sure only your skill and the request shape the answer, not what you said before.
Do:
1. Open a **new chat**, with memory or personal context off if you can.
2. Send **test 1** with its sample and note whether the answer **follows your skill**.
3. Compare the output with what you **expected** and mark pass or fail.
4. Repeat for **test 2** and **test 3**, each in a new chat.
Ask: Send your results: each test, pass or fail, and what came out where it failed.

### Run [no-skills]
Why: A **fresh chat** for each test makes sure only your skill and the request shape the answer, not what you said before.
Do:
1. Open a **new chat in your project** or Gem and send **test 1** with its sample.
2. Do the same for **test 2**, then mark pass or fail against what you **expected**.
3. For **test 3**, open a plain new chat, paste only your **name and description** and the request, and ask: "Would this skill apply? Yes or no."
Ask: Send your results: each test, pass or fail, and what came out where it failed.

### Fix
Why: Make **one change per failure**, so you can see which change worked. If you rewrite everything, or add a new rule for every problem, the skill gets longer and old rules start to contradict each other (this pile-up is called **[[sediment]]**).
Do: For each failed test, name the **part** that caused it (description, instructions, format or missing rule) and write the **new line** that replaces the old one.
Ask: Send each failure, the part, the old line and the new line; your full **skill v3** appears on the page.
Code:
```text
Test [n] failed: [what came out]. Part: [description / steps / format / missing rule]
Old: [old line]
New: [new line]
```
Example:
```text
Test 3 failed: the sales email loaded the skill. Part: description, "emails" is too broad.
Old: Use when the user asks for an email reply.
New: Use when the user pastes a customer complaint. Do not use for sales or marketing emails.
```
Weak:
```text
The skill is not good enough yet, so I rewrote all of it.
```

### Go further [fast-track]
Why: The AI does not choose the same way every time, so **one** passing run proves little, and a run **without** the skill shows what the skill adds.
Do: Run your **near miss three times** and **test 1 once with the skill switched off**; note any run that differs.
Ask: Send how many of the three near-miss runs passed, and what the run without the skill was missing.

## Trust check
Watch for:
- Test with **made-up or anonymised** material, never a real customer's message. (GDPR, Article 5)
- Count a test as passed only when the output matches what you **wrote down before** the run. (EU AI Act, Article 4)
- Install only skills you **wrote yourself** or got from a trusted source, and read every file first. (Anthropic skill security)
Rules:
- GDPR, Article 5: Personal data must be adequate, relevant and limited to what is necessary for the purpose it is used for. [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- EU AI Act, Article 4: Organisations that provide or use AI systems must make sure their staff have enough AI literacy for their role: they understand the tools and what the outputs mean. [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- Anthropic skill security: Only use skills you created or got from a trusted source, and check every file first, because a skill can run code. [Anthropic docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
Ask: After these tests, how closely will you **check** this skill's output next week?

## Test
Do: Paste your **fixed skill** into a **fresh chat** with "Follow this skill for my next message" and run each **failed test** again. Only if you changed the **description**, update the installed skill (ask Claude for the new ZIP) and send the near miss again.
Check:
- Every test that **failed** before now passes.
- The **near miss** stays quiet, also when you write it **in new words**.
- Each change fixed **one failure** you can name.
Ask: Did the failed tests pass with the fixed version? Tell me which one still failed, if any, and what came out.

## Test [claude-code]
Do: Edit **SKILL.md** in place, start a **new session** in a folder without a CLAUDE.md, then run each **failed test** and the **near miss** again, each in a new session.
Check:
- Every test that **failed** before now passes.
- The **near miss** stays quiet, also when you write it **in new words**.
- Each change fixed **one failure** you can name.
Ask: Did the failed tests pass with the fixed version? Tell me which one still failed, if any, and what came out.

## Test [gemini]
Do: In **Settings > Skills**, edit the description or instructions and **Save**, then run each **failed test** and the **near miss** again, each in a **new chat**.
Check:
- Every test that **failed** before now passes.
- The **near miss** stays quiet, also when you write it **in new words**.
- Each change fixed **one failure** you can name.
Ask: Did the failed tests pass with the fixed version? Tell me which one still failed, if any, and what came out.

## Test [no-skills]
Do: Update the **project or Gem instructions** with the fixed version, run each **failed test** in a new chat there, and repeat the **description check** for the near miss.
Check:
- Every test that **failed** before now passes.
- The description check says **no** for the near miss, also **in new words**.
- Each change fixed **one failure** you can name.
Ask: Did the failed tests pass with the fixed version? Tell me which one still failed, if any, and what came out.

## Other ways
- Call it by name: Ask for your skill by name in a chat to test the steps apart from the automatic start.
- skill-creator: Ask Claude to **use the skill-creator** to run your tests with and without the skill and show the results side by side.
- Two chats: Keep **one chat** for improving the skill and a **fresh chat** for testing it, so the test never sees your explanations.

## Other ways [claude-code]
- Call it by name: Run **/[name]** with each sample to test the instructions apart from the trigger.
- skill-creator: Ask Claude Code to **use the skill-creator** to run your tests with and without the skill and compare them.
- Project skill: Save the folder in **.claude/skills/** of one project, so the skill loads only there.

## Other ways [chatgpt]
- Call it by name: Type **@[name]** in the message to run your skill on purpose and test the instructions apart from the trigger.
- Codex: Save the folder in **~/.agents/skills/**, call it with **$[name]**, and use **$skill-creator** to draft more tests.
- Editor: Open the Skills editor to change the skill **without a new upload**.

## Other ways [gemini]
- Call it by name: Type **/** and choose your skill to test the instructions apart from the automatic choice.
- Gemini CLI: Save the folder in **~/.gemini/skills/**; the CLI asks before it **loads a skill**, so you see each time it is used.
- Edit in place: In **Settings > Skills**, change the description or instructions and **Save**.

## Other ways [no-skills]
- Prompt library: Keep the SKILL.md as a file and paste it into a fresh chat for each test.
- Claude: The same SKILL.md uploads in Claude on any plan, including Free, if you want to test the trigger for real.
- Later: When your tool or plan gets skills, run the near-miss test again for real.

## Done when
- Your test sheet has 3 requests, each with an expected result written before the run.
- Each failure has a named part and one changed line.
- The fixed skill is installed and passes the tests that failed before.

## Practice
- Switch the skill **off**, run test 1 again and note what the skill adds: this is your **[[baseline]]**.
- Add one real request from this week that surprised you as a fourth test.
- Write a second near miss in other words and check that the skill stays quiet.

## Reusable template
Name: Skill test and fix sheet
```text
Skill: [name], v2 > v3

1. Normal: "[request]" + [short sample]
   Expect: [skill loads] + [what a good output contains]
   Result: [pass / fail: what came out]
2. Awkward: "[request]" + [incomplete or unusual sample]
   Expect: [skill loads] + [asks for ... / handles ...]
   Result: [pass / fail: what came out]
3. Near miss: "[similar request that is not this task]"
   Expect: skill does not load
   Result: [pass / fail]

Failure > part > change: [test] > [description / instructions / format / missing rule] > [new line]
Re-test with v3: [pass / fail]
```

## Glossary
- Test set: A short list of requests with the result you expect, used every time you change a skill.
- Near miss: A request that looks similar to your task but needs a different result, so the skill must not load.
- Baseline: The same request run without the skill, to see what the skill adds.
- Missing rule: An instruction a skill needs but does not have, often for what to do when information is missing.
- Sediment: Old rules that pile up in a skill over time and no longer change what it does.

## Sources
- [Claude Help Centre: Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude): The plans that include skills (Free to Enterprise) and the exact menu path to upload a ZIP.
- [Claude Help Centre: How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills): The ZIP structure: the skill folder must sit at the top of the ZIP.
- [Anthropic: Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices): Build at least 3 evaluations and compare with a run without the skill.
- [Anthropic: skill-creator skill](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md): Anthropic's own process for testing a skill with and without it.
- [Anthropic: The complete guide to building skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf): Trigger tests and a concrete target: the skill loads for at least 90 % of the requests it should.
- [Anthropic: Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview): Why to install only skills from trusted sources.
- [Matt Pocock: Building Great Agent Skills (AI Engineer)](https://www.youtube.com/watch?v=UNzCG3lw6O0): Why rules pile up as sediment, and the deletion test for lines that change nothing.

## Coach notes
Arc: third of five in this topic (write the skill; install it and add an example; test and fix; reference files and templates; connect and get ready to share). Never name the other missions by number to the learner. Levels covered: test and fix.
No failures: if every test passed, the learner writes one harder awkward test (two missing details, or input in another language) and runs it first. If that passes too, the Fix step becomes a near-miss rephrasing test; say so plainly.
Diagnosis: wrong skill or no skill loaded means the description; right skill but wrong steps means the instructions; right steps but wrong shape means the format; invented details mean a missing "ask, never guess" rule. A rule that exists but does not reach this case counts as a missing rule: widen it, do not add a second one. Several failures: fix the one that changes the most first.
Levels: guided (A, B) shapes three tests with your questions and sees the step's example before writing; standard (C) writes the tests alone; fast-track (D) may test out with an existing test sheet and a fixed version, and gets the Go further step (repeated runs, run without the skill).
Guided mode (default for beginners): before a beginner writes each part, point to the step's "See an example" on the page, say in one sentence why it works (for example: "it names a near miss"), then ask for their version for their own case. Some familiarity: they try first and you point to the example after the first try. Experienced: only when they ask. The example is from a different case, so they adapt it instead of copying it; if they copy it word for word, ask what changes for their task. Beginners can also take the working example instead of their own task, so the page example and their task differ only in the details.
Starter skill: if the learner has no skill yet and chose the working example, draft a short skill for the working example adapted to their role. Say you drafted it for them and that it has at least one weak spot their tests should find (for example a description without a near miss). This is a test object, not their artefact.
Likely errors: the expected result is written after the run, so every output passes; the awkward test is complete and clean; the near miss is too different to test anything ("write a poem"); tests run in the chat where the skill was written, so context leaks in; the learner pastes the SKILL.md into the chat instead of uploading it, which tests the instructions but not the trigger.
Upload problems: see the install mission's notes; the most common are a ZIP with a folder inside a folder and a file saved as SKILL.md.txt.
Cannot upload today (no permission, admin block): do the closest honest substitute and say so. For the trigger, open a fresh chat, paste only the name and description plus the request, and ask "Would this skill apply to this request? Yes or no." Label it a proxy on the test sheet. For tests 1 and 2, paste the whole skill into a fresh chat.
Skills that use a connector or MCP tool: test them in the tool where that connector works (often Claude Code or Cowork), not in plain chat.
Time budget for guided learners (30 minutes in total, profile and level question included): about 4 to 5 minutes per build step. They copy the step's fill-in lines and fill the [blanks]; they never write a part from an empty page. If a step runs over 8 minutes, accept a short version and note one improvement for later. The coach may give made-up test samples (5 lines each) for the learner's task: they are test material, not the learner's artefact.
Time: allow at most two feedback rounds per step. Expected results stay short (one line each).
Feedback: name the test that is well written, then the one that tests nothing, then one fix.
Trust question: push for a concrete answer tied to their work ("I check every figure for the next four weeks"), not "I will be careful".
Page state: set the full skill v3 as the part for the last step (Fix; Go further for fast-track).
Other vendors: in ChatGPT (eligible Business, Enterprise and Edu workspaces) and the Gemini app the same three tests work; the near-miss test applies only where the skill loads automatically from its description.
