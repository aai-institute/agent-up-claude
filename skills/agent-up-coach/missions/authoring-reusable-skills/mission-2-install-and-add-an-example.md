---
id: mission-2-install-and-add-an-example
number: 2
title: Install your skill and add an example
summary: Install your skill so it loads by itself, and add one example of a good result and a rule for an unusual case. You leave with a skill that is installed and more reliable.
artefact: "Skill v2: installed SKILL.md with an example and an edge rule"
---

Track: Baseline
Level: foundation
Time: 30 minutes
Tools: Claude chat, Cowork or Claude Code
Artefact kind: text
Artefact file: my-skill-v2.md

## Context
Your skill works when you attach or paste it, but you have to remember to, and the results still vary in length and tone. **Installed** with one **example**, it starts by itself and gives the result you mean.

## Your task
Add **one [[example]]** of a good result and **one [[edge rule]]** for an unusual case to your skill, then **[[install]]** it and check that it starts for the right request.

## After this, you can
Show an AI the result you want with one example, and install a skill so it loads by itself.

## You need
- Your **SKILL.md** with a name, description, steps and checks, or the **working example** in this mission
- **Claude** on any plan, with permission to turn on skills

## You need [claude-code]
- Your **SKILL.md** with a name, description, steps and checks, or the **working example** in this mission
- **Claude Code** and a folder **without** project files

## You need [chatgpt]
- Your **SKILL.md** with a name, description, steps and checks, or the **working example** in this mission
- **ChatGPT** in a Business, Enterprise, Healthcare or Edu workspace where your admin allows **skill uploads**

## You need [gemini]
- Your **SKILL.md** with a name, description, steps and checks, or the **working example** in this mission
- The **Gemini app** with a personal Google account (18 or older, **Keep Activity** on)

## You need [no-skills]
- Your **SKILL.md** with a name, description, steps and checks, or the **working example** in this mission
- Your usual **AI chat** with **projects** (ChatGPT) or **Gems** (Gemini)

## You should already
- Be able to write a **SKILL.md** with a name, description, steps and checks

## Concept
Heading: The 2 things that make a skill reliable
Lead: Steps say **what to do**. An example and an edge rule show **what good looks like** and what to do when the input is **not normal**.
- Example: One short **input and the good result** for it. The AI copies its length, tone and structure.
- Edge rule: One rule for the **unusual case** you meet most often: missing data, another language, a very long input.
Close: Steps say what to do; the **example** shows the result, and the **edge rule** covers the case that goes wrong most often.

## Check your understanding
Question: Your skill writes replies that are too long, although the steps say "keep it short". What helps most?
- A: Write "very short" in capital letters
- B: Add one example of a good reply with the right length
- C: Add three more steps about length
- D: Remove the output format
Answer: B
Why: "Short" means different things to the AI and to you. One example shows the length you mean. A and C add words without showing the result; D removes the little guidance there was.

## Working example
Situation: Your **status update skill** works, but the updates are longer each week, and once a project had **no update at all**.
Input: Your **skill v1** and one Friday update you were happy with, names removed.
- Add the good update as an **example** at the end of the skill.
- Add a rule: if a project has **no update**, write "no update this week" and ask.
- **Install** the skill in Claude.
- Check it starts for "write my Friday update" and **not** for "write meeting minutes".
Result: An **installed skill v2** that writes updates like your example.
Ask: Do you want to work on a skill you wrote, or on the working example? If you have no skill yet, say so and I will give you a short one to start from.

## Steps
### Example
Use: Work on a skill you wrote, or on the working example below.
Why: One example sets **length, tone and structure** at once; without it, the AI guesses what you mean by "short" or "clear".
Do: Add **one short example** at the end of your skill: a typical **input** and the **good result** you want for it. Use a result you **already have** and change the names.
Ask: Send the example you added.
Code:
```text
# Example
Input: [a typical input, 2 to 4 lines, names made up]
Good result: [a result you were happy with, names made up]
```
Example:
```text
# Example
Input: "Order 4471 arrived broken. I need it by Friday."
Good reply: "I am sorry your order 4471 arrived broken. We are sending a new one today; it arrives by Thursday. Questions: [support address]."
```
Weak:
```text
# Example
Write a good reply, like our best ones.
```

### Edge rule
Why: Most failures come from the **unusual case**: if the skill has no rule for it, the AI improvises.
Do: Name the **unusual case** you meet most often in this task and add **one rule** for it: what the AI should do instead of improvising.
Ask: Send the unusual case and your rule.
Code:
```text
# When the input is unusual
- If [the unusual case], [what to do instead]. If unsure, ask.
```
Example:
```text
Unusual case: the complaint is in another language.
Rule: Reply in the language of the complaint. If you are not sure which language it is, ask.
```
Weak:
```text
Handle special cases well.
```

### Install
Why: A skill pasted into a chat works only in that chat. **Installed**, the AI sees its description in **every** chat and starts it by itself when a request matches.
Do:
1. In Claude, open **Settings > Capabilities** and turn on **Code execution and file creation**.
2. In a new chat, paste your skill and ask: **"Save this as SKILL.md in a folder named [name] and give me the folder as a ZIP."** Download the ZIP.
3. If that does not work, ask in the chat for the by-hand way. Claude's ZIP holds the folder with your **[[header]]** at the top of SKILL.md, packed into one **[[ZIP file]]**.
4. Open **Customize > Skills**, press **+**, choose **Upload a skill** and select your ZIP.
5. Check that the skill shows in the list and is **switched on**.
Ask: Tell me when your skill shows in the list, or which message you see.

### Install [claude-code]
Why: A skill pasted into a chat works only in that chat. **Installed**, the AI sees its description in **every** chat and starts it by itself when a request matches.
Do:
1. Create the folder **~/.claude/skills/[name]/** with the command below.
2. Save **only your skill** in it as **SKILL.md**: the file starts with the **---** line of your header.
3. Start **claude** in a folder without project files.
4. Type **/skills** and check that your skill is in the list.
Code:
```bash
mkdir -p ~/.claude/skills/[name]
```
Ask: Tell me when your skill shows in the list, or which message you see.

### Install [chatgpt]
Why: A skill pasted into a chat works only in that chat. **Installed**, the AI sees its description in **every** chat and starts it by itself when a request matches.
Do:
1. Create a folder named **exactly like your skill's name** and save **only your skill** in it as **SKILL.md**.
2. Compress the **folder** into a **ZIP** file.
3. In ChatGPT, open **Plugins** in the sidebar, then the **Skills** tab.
4. Choose **Create**, then **Upload from your computer**, and select your ZIP.
5. Wait for the **scan** to finish and check that the skill is in your list.
Ask: Tell me when your skill shows in the list, or which message you see.

### Install [gemini]
Why: A skill pasted into a chat works only in that chat. **Installed**, the AI sees its description in **every** chat and starts it by itself when a request matches.
Do:
1. Create a folder named **exactly like your skill's name** and save **only your skill** in it as **SKILL.md**.
2. In the Gemini app, open **Settings**, then **Skills**.
3. Choose **Create** and upload your **skill folder** or its SKILL.md.
4. Select the skill, open **More** and choose **Activate**.
Ask: Tell me when your skill shows as active, or which message you see.

### Install [no-skills]
Why: Your tool has **no automatic trigger**, so a project or Gem holds the instructions, and the near miss becomes a **description check**.
Do:
1. Create a **project** (ChatGPT) or a **Gem** (Gemini) named like your skill.
2. Paste your skill's **instructions** into its instructions field, everything below the header.
3. Save it and keep your **name and description** in a note for the near-miss test.
Ask: Tell me when your project or Gem is saved, or which message you see.

### Go further [fast-track]
Why: Steps differ in how much **freedom** they need: open steps work best with a goal, fragile steps with exact wording.
Do: Mark each step of your skill as **goal** (several good ways), **pattern** (one preferred way) or **exact** (must always be the same), and rewrite one exact step word for word.
Ask: Send your marked steps and the rewritten exact step.
Example:
```text
1. Name the problem in one sentence: goal
2. Apology: pattern ("I am sorry that ...")
3. Refund amount: exact. "Copy the amount from the price list. Never calculate or round it."
```

## Trust check
Watch for:
- Make up the **example**: no real names, order numbers or client details. (GDPR, Article 5)
- Install only skills you **wrote yourself** or got from a trusted source, and read every file first. (Anthropic skill security)
Rules:
- GDPR, Article 5: Personal data must be adequate, relevant and limited to what is necessary for the purpose it is used for. [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- Anthropic skill security: Only use skills you created or got from a trusted source, and check every file first, because a skill can run code. [Anthropic docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
Ask: Is anything in your example **real** data that should be made up?

## Test
Do: In a **fresh chat**, send a request your skill should handle with a short sample; then, in another fresh chat, send a **similar request** it should ignore.
Check:
- Claude shows that it **uses your skill** for the first request, without you naming it.
- The similar request runs **without** your skill.
Ask: Did your skill start for the right request only?

## Test [claude-code]
Do: Start a **new session** in a folder without a CLAUDE.md, send a request your skill should handle; then, in another new session, send a **similar request** it should ignore.
Check:
- Claude Code shows that it **uses your skill** for the first request, without you naming it.
- The similar request runs **without** your skill.
Ask: Did your skill start for the right request only?

## Test [no-skills]
Do: In a new chat in your project or Gem, send a request with a short sample; then, in a plain new chat, paste only your **name and description** with a similar request and ask "Would this skill apply? Yes or no."
Check:
- Your **edge rule** works when you send the unusual case.
- The description check says **no** for the similar request.
Ask: What came out in both chats?

## Other ways
- Cowork: Ask Cowork to **save your skill** as a folder and ZIP in your connected folder, then upload it.
- Call it by name: Ask for your skill by its name in a chat to run it on purpose.
- skill-creator: Ask Claude to **use the skill-creator** to suggest a better example for your skill.

## Other ways [claude-code]
- Call it by name: Type **/[name]** to run your skill on purpose, even when the description would not start it.
- Project skill: Save the folder in **.claude/skills/** of one project, so it loads only there.
- Claude apps: Upload the same folder as a ZIP in **Customize > Skills** to use it in Claude chat too.

## Other ways [chatgpt]
- Call it by name: Type **@[name]** to run your skill on purpose.
- Editor: Change the skill in the **Skills editor** without a new upload.
- Codex: Save the folder in **~/.agents/skills/** and call it with **$[name]**.

## Other ways [gemini]
- Call it by name: Type **/** and choose your skill.
- Edit in place: In **Settings > Skills**, change the instructions and **Save**.
- Gemini CLI: Save the folder in **~/.gemini/skills/**.

## Other ways [no-skills]
- Prompt library: Keep SKILL.md as a file and paste it into a fresh chat when the task comes up.
- Claude: The same SKILL.md uploads as a skill in Claude on any plan, including Free.
- Later: When your tool gets skills, the same file works without changes.

## Done when
- Your skill has one made-up example of a good result and one rule for an unusual case.
- The skill is installed and switched on.
- It started for the right request and not for the similar one.

## Practice
- Send the unusual case from your edge rule and check that the rule works.
- Replace your example with a better one from this week, names made up.
- Write a second similar request in other words and check that the skill stays quiet.

## Reusable template
Name: Example and edge rule
```text
# Example
Input: [a typical input, made up]
Good result: [the result you want, with the right length and structure]

# When the input is unusual
- If [the unusual case], [what to do instead]. If unsure, ask.
```

## Glossary
- Example: A short input with the good result for it, added to a skill so the AI copies its length, tone and structure.
- Edge rule: A rule in a skill for the unusual case you meet most often, so the AI does not improvise.
- Install: Adding a skill to your AI tool so it is always visible and can start by itself.
- ZIP file: One compressed file that holds a whole folder, used to upload a skill in one go.
- Header: The block between the two --- lines at the top of SKILL.md, with the name and description.

## Sources
- [Anthropic: Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices): Input and output examples help the AI match the style and detail you want.
- [Claude Help Centre: Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude): The plans that include skills and the menu path to upload a ZIP.
- [Claude Help Centre: How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills): The ZIP structure: the skill folder must sit at the top of the ZIP.
- [Anthropic: Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview): Why only the name and description are always visible, and why to install only trusted skills.
- [Google: Skills in the Gemini app](https://support.google.com/gemini/answer/17094296): How to create and activate a skill in the Gemini app.

## Coach notes
Arc: second of five in this topic (write the skill; install it and add an example; test and fix; reference files and templates; connect and get ready to share). Never name the other missions by number to the learner. Levels covered: guard (example, edge rule) and install.
Levels: guided (A, B) sees each step's example before writing, gets Claude to build the ZIP, and hears plain words only (say "the block at the top" for header); standard (C) tries first; fast-track (D) may test out with an installed skill that has an example, and gets the Go further step.
Starter skill: if the learner has no skill yet, draft a short v1 for the working example adapted to their role and say you drafted it. The example and the edge rule stay theirs.
Likely errors: an example that describes quality instead of showing a result; a real email pasted as the example; an edge rule for a rare case instead of the most common one; the ZIP holds a folder inside a folder; the file is saved as SKILL.md.txt.
Menus: if the learner's app shows other menu names than the page, ask what they see and guide from there; menu names change between app versions.
Upload problems: "SKILL.md.txt" (Windows hides extensions: let Claude build the ZIP); "contents zipped instead of the folder"; an error that says "frontmatter" means the header block at the top; "folder name does not match" (rename the folder to the name); "invalid characters" (capitals, spaces, umlauts in the name). On Team or Enterprise an admin may need to enable skills. Menu names change; ask what they see.
Cannot upload today: paste the skill into a fresh chat to check the example, and use the description check ("Would this skill apply? Yes or no.") for the similar request; label both as stand-ins.
Time budget for guided learners (30 minutes in total, profile and level question included): about 4 to 5 minutes per build step. They copy the step's fill-in lines and fill the [blanks]; they never write a part from an empty page. If a step runs over 8 minutes, accept a short version and note one improvement for later.
Time: two feedback rounds per step at most. The test checks only what this mission changed: does the installed skill start by itself for the right request and stay quiet for the similar one. Output quality is not re-checked here; the full test set comes in the test-and-fix mission.
Page state: set the full skill v2 as the part for the last step (Install; Go further for fast-track).
Other vendors: ChatGPT (eligible workspaces) and the Gemini app read the same SKILL.md; the description starts the skill only where skills load automatically.
