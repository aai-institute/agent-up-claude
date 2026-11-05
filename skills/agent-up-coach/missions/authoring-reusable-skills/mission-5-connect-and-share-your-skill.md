---
id: mission-5-connect-and-share-your-skill
number: 5
title: Connect your skill and get it ready to share
summary: Let your skill read from an app you already connect to Claude, limit what it may do, and package it with a version and a short card so others can use it.
artefact: "Skill v5: connected skill with a guard, version line and card"
---

Track: Baseline
Level: practitioner
Time: 30 minutes
Tools: Claude chat, Cowork or Claude Code, with one connected app
Artefact kind: text
Artefact file: my-skill-v5.md

## Context
You still **copy data in** from your drive by hand, and nobody else could use your skill without asking you first. **Connecting** one step, a **guard** and a short **card** solve both.

## Your task
Let one step of your skill **read from a connected app**, add a **guard** for what it may do, and write a **version line and a card** so someone else could use it.

## After this, you can
Connect one step of a skill to an app with a clear limit, and prepare a skill so someone else can use it without asking you.

## You need
- Your **skill folder**, tested at least once, or the **working example** in this mission
- **Claude** with skills switched on and one **connected app** you may use at work (for example Google Drive or a calendar)
- **Test data** in that app, or a copy with names removed

## You need [claude-code]
- Your **skill folder**, tested at least once, or the **working example** in this mission
- **Claude Code** and one **MCP server** or connected tool you may use at work
- **Test data**, or a copy with names removed

## You need [chatgpt]
- Your **skill folder**, tested at least once, or the **working example** in this mission
- **ChatGPT** in a workspace with **skills** and one **connected app** your admin allows

## You need [gemini]
- Your **skill folder**, tested at least once, or the **working example** in this mission
- The **Gemini app** with skills and a **connected Google app** (Drive, Calendar or Gmail)

## You need [no-skills]
- Your **skill folder**, tested at least once, or the **working example** in this mission
- Your **project** or **Gem**, and one **connected app** your tool offers, or a file export of the data

## You should already
- Be able to **install a skill** and run a test in a **fresh chat**

## Concept
Heading: The 3 things a skill needs before others rely on it
Lead: A skill that fetches its own data and that other people use needs **a connection**, **a limit** and **a card**.
- Connection: One step reads **live data** from a **[[connected app]]** you already use with Claude, such as a drive or calendar, instead of you pasting it.
- Guard: A **[[guard]]**: rules for what the skill may **read** and what it must **ask before** doing: sending, saving, deleting.
- Card: A **[[skill card]]**, one page **next to** the skill folder: what it does, when to use it, what to check, who looks after it.
Close: Each of the three gets its own step below, with its reason.
Toggle: Is a connected skill an automation? | No. A skill still runs only when someone **asks** for it. Automations that run **on their own**, on a schedule or an event, are a separate topic.
Toggle: Why is the card next to the folder, not inside it? | Everything **inside** the folder is read by the AI. The card is for **people**, so it lives next to the folder.

## Check your understanding
Question: Your skill reads this week's meetings from a connected calendar and drafts a summary. Which guard rule matters most?
- A: Be careful with the calendar
- B: Read only; never create, change or delete events; show any draft before sending it
- C: Use the calendar as often as possible
- D: No guard is needed, because the calendar is connected
Answer: B
Why: B names what the skill may read and what it must never do or must ask about. A is too vague to follow, C adds risk, and D ignores that a connection reaches real data.

## Working example
Situation: Your **status update skill** needs this week's tasks, which you copy by hand from a **shared task list** in your drive. Two other team leads want to use the skill too.
Input: Your **tested skill folder** and the task list in your connected drive, with test tasks only.
- Rewrite the task step to **read** the list from the drive.
- Add a **guard**: read only, ask before saving or sending anything.
- Replace project names with **[placeholders]** and add a **version line**.
- Write a short **card** for the two team leads.
Result: A **skill v5** that fetches its own input and is ready to share.
Ask: Do you want to work on a skill of your own, or the working example? Tell me which data you still copy in by hand.

## Steps
### Connect
Use: Work on a skill you wrote, or on the working example below.
Why: Copying data in by hand is where mistakes and old versions creep in; a step that **names the app** and says **exactly what to read** lets the skill fetch it itself.
Do:
1. Choose the **one step** where you still copy data in by hand. If the app is **not connected yet** or not allowed, upload a **file** with the same data to the chat instead.
2. In Claude, open **Customize > Connectors** (Claude calls connected apps "connectors") and connect the app that holds the data.
3. In a chat, open **+ > Connectors** and make sure the app is **switched on**.
4. In SKILL.md, rewrite the step to **name the app** and say exactly **what to read**, and what to do when the app is **not available**.
Ask: Send your rewritten step and the line for when the app is not available.
Code:
```text
[n]. Read [what exactly] from [app name], [folder or file]. Use only what it returns.
     If [app name] is not available, say so and ask me for the data. Never invent it.
```
Example:
```text
2. Read the delivery status from Google Drive, sheet "Orders this month", row with the order number. Use only the column "Status".
   If Google Drive is not available, say so and ask me for the status. Never invent it.
```
Weak:
```text
2. Get the data from Drive.
```

### Connect [claude-code]
Use: Work on a skill you wrote, or on the working example below.
Why: Copying data in by hand is where mistakes and old versions creep in; a step that **names the tool** and says **exactly what to read** lets the skill fetch it itself.
Do:
1. Choose the one step that needs **live data** from another system (an issue tracker, a drive, a database).
2. Connect that system as an **MCP server** in Claude Code, or use one you already have.
3. Rewrite the step to **name the tool** (ServerName:tool_name) and say exactly **what to read**.
4. Add what to do when the tool is **not available**: say so and ask, never invent the data.
Ask: Send your rewritten step and the line for when the tool is not available.
Example:
```text
2. Read the open issues labelled "release" with GitHub:list_issues. Use only title and number.
   If GitHub is not available, say so and ask me for the list. Never invent issues.
```
Weak:
```text
2. Check GitHub.
```

### Connect [chatgpt]
Use: Work on a skill you wrote, or on the working example below.
Why: Copying data in by hand is where mistakes and old versions creep in; a step that **names the app** and says **exactly what to read** lets the skill fetch it itself.
Do:
1. In ChatGPT, connect the **app** your step needs (your admin decides which apps exist).
2. In your skill, rewrite your chosen step to **name the app** and say exactly **what to read**.
3. Add what to do when the app is **not available**: say so and ask, never invent the data.
4. Update the skill in the **Skills editor** or upload it again.
Ask: Send your rewritten step and the line for when the app is not available.

### Connect [gemini]
Use: Work on a skill you wrote, or on the working example below.
Why: Copying data in by hand is where mistakes and old versions creep in; a step that **names the app** and says **exactly what to read** lets the skill fetch it itself.
Do:
1. In the Gemini app, check that the **Google app** your step needs (Drive, Calendar or Gmail) is connected.
2. In **Settings > Skills**, rewrite your chosen step to **name the app** and say exactly **what to read**.
3. Add what to do when the app is **not available**: say so and ask, never invent the data.
4. **Save** the skill. Scripts in Gemini app skills cannot call external websites, so keep web steps out of scripts/.
Ask: Send your rewritten step and the line for when the app is not available.

### Connect [no-skills]
Use: Work on a skill you wrote, or on the working example below.
Why: Copying data in by hand is where mistakes and old versions creep in; a step that **names the app** and says **exactly what to read** lets the skill fetch it itself.
Do:
1. Connect the **app** your step needs in your AI tool, if it offers connected apps.
2. In your project or Gem instructions, rewrite the step to **name the app** and say exactly **what to read**.
3. Add what to do when the app is **not available**: say so and ask, never invent the data.
Ask: Send your rewritten step and the line for when the app is not available.

### Guard
Why: The app lets the skill reach your **real files and data**. A guard is a rule in the skill that keeps it to **reading**, and makes it **ask you** before it sends, saves or deletes anything. What the app can reach at all is set by your account and your admin.
Do: Add a **guard** section: what the skill may **read**, that it **asks before** any write, send or delete, and a **[VERIFY]** flag on what the app returns.
Ask: Send your guard lines.
Code:
```text
# Guard
- Read only: [what]. Never [change / send / delete] [what].
- Before sending or saving anything, show the draft and wait for "yes".
- [VERIFY] [what the app returned] matches [where you can check it].
```
Example:
```text
# Guard
- Read only: order status and delivery date from the shop system. Never change an order.
- Before sending or saving anything, show the draft and wait for "yes".
- [VERIFY] The order number in the reply matches the one the shop system returned.
```
Weak:
```text
Be careful with the shop system.
```

### Card
Why: Other people decide in **one minute** whether to use a skill, and they cannot ask you; a version line tells everyone **which copy** is current.
Do: Replace names, client details and links in the folder with a **[[placeholder]]** each, add a last line with **version, owner and date**, and write a **one-page card** next to the folder.
Ask: Send your **card**; the version line goes at the end of your skill on the page.
Code:
```text
[skill-name], version [n], owner: [team or role], checked [month year]
Does: [what, for whom]. Use when: [situations]. Not for: [near miss].
Check before using: [VERIFY items]. Needs: [app, access].
```
Example:
```text
Version 1.0, owner: Customer Service team lead, checked October 2026.

Card: complaint-reply-drafts, version 1.0
Does: drafts replies to customer complaints in our support tone.
Use when: you paste a complaint email. Not for: sales or internal emails.
Fill in: [support address] in the template.
Check before sending: every refund amount and date (marked [VERIFY]).
Needs: Claude with skills; shop system connector, read only.
```
Weak:
```text
A skill for replies. Ask me if anything is unclear.
```

### Go further [fast-track]
Why: Some steps must give **exactly the same result** every time, and some skills should run **only when called** by name.
Do: Add one **script** in scripts/ for an exact step (run it once on test data and check the result by hand), or, in Claude Code, add **disable-model-invocation: true** to the header if the skill should run only as /[name].
Ask: Send your script and its test result, or your header with the reason.

## Trust check
Watch for:
- Connect with the **least access** the step needs, test data first, and never put passwords or keys in the skill. (GDPR, Article 5)
- Keep a **person in the loop**: the skill asks before it sends, saves or deletes anything. (EU AI Act, Article 4)
- Before you install a skill **someone else** wrote, read every file and look for scripts and web addresses. (Anthropic skill security)
Rules:
- GDPR, Article 5: Personal data must be adequate, relevant and limited to what is necessary for the purpose it is used for. [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- EU AI Act, Article 4: Organisations that provide or use AI systems must make sure their staff have enough AI literacy for their role: they understand the tools and what the outputs mean. [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- Anthropic skill security: Only use skills you created or got from a trusted source, and check every file first, because a skill can run code and fetch web content. [Anthropic docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
Ask: Which data does your connected step **read**?

## Test
Do: In a **fresh chat** with the app connected, send one request that needs the connected step; then switch the app **off** for the chat and send it again.
Check:
- With the app on, the result uses the **live data** and the skill **asks** before any change.
- With the app off, the skill **says it cannot reach** the app instead of inventing data.
- Someone reading only your **card** would know when to use the skill and what to check.
Ask: What happened with the app on and off? Tell me what came out.

## Test [claude-code]
Do: Start a **new session**, send one request that needs the connected step; then, in another new session with the tool turned off, send it again.
Check:
- With the tool on, the result uses the **live data** and the skill **asks** before any change.
- With the tool off, the skill **says it cannot reach** it instead of inventing data.
- Someone reading only your **card** would know when to use the skill and what to check.
Ask: What happened with the tool on and off? Tell me what came out.

## Test [no-skills]
Do: In a new chat in your project or Gem, send one request that needs the connected step; then send it again in a chat **without** the app or file.
Check:
- With the app or file, the result uses its **data** and asks before any change.
- Without it, the result **says the data is missing** instead of inventing it.
- Someone reading only your **card** would know when to use the skill and what to check.
Ask: What happened in both chats? Tell me what came out.

## Other ways
- Team and Enterprise: Use the skill's **share** option, or ask an admin to publish it to your **organisation library**.
- Other plans: Share the **ZIP and the card** through a shared drive; each person uploads it in **Customize > Skills**.
- File instead of an app: Upload a **file export** with the skill to test the step before you connect anything.

## Other ways [claude-code]
- Project skill: Commit the folder to **.claude/skills/** in your team's repository, so everyone who works there gets it.
- Plugin: Bundle the skill in a **plugin** for your team; skills in a plugin are called as plugin-name:skill-name.
- Allowed tools: **allowed-tools** in the header pre-approves tools; to block a tool, use permission rules in your settings.

## Other ways [chatgpt]
- Workspace: Use **Share skills** or ask an admin to **publish** the skill to your workspace.
- Plugins: In ChatGPT a skill can sit next to apps in a **plugin**; the app brings the data, the skill the workflow.
- Codex: Commit the folder to **.agents/skills** in a shared repository.

## Other ways [gemini, no-skills]
- Shared drive: Keep the **ZIP and the card** in one shared folder, with the version in the file name.
- File instead of an app: Upload a **CSV export** with the skill to test the step first.
- Claude: The same folder uploads as a skill in Claude on any plan, with connectors.

## Done when
- One step names the connected app, says what to read and what to do when the app is not available.
- A guard limits the skill to reading and makes it ask before any change.
- The folder holds no personal data, ends with a version line, and has a one-page card next to it.

## Practice
- Read every file of one skill you did not write before you install it, and note any script or web address.
- Run your skill once with real data, read only, and compare the result with what you would have written by hand.
- Put a date in your calendar to check your skill and its card again in three months.

## Reusable template
Name: Connected step, guard and card
```text
[n]. Read [what exactly] from [app name]. Use only what it returns.
     If [app] is not available, say so and ask me for the data. Never invent it.

# Guard
- Read only: [what]. Never [change / send / delete] [what].
- Before sending or saving anything, show the draft and wait for "yes".
- [VERIFY] [app result] matches [where a person can check it].

Version [n], owner: [team or role], checked [month year].

Card: [skill-name], version [n]
Does: [what, for whom]. Use when: [situations]. Not for: [near miss].
Fill in: [placeholders]. Check: [VERIFY items]. Needs: [tool, app, access].
```

## Glossary
- Connected app: An app such as a drive or calendar that you link to your AI tool, so it can read data or take actions there.
- Guard: A section in a skill that limits what it may read and change, and when it must ask first.
- Skill card: A one-page note next to a skill folder that tells people what the skill does, when to use it and what to check.
- Placeholder: A marked gap such as [client] that replaces real data in a shared skill.

## Sources
- [Claude Help Centre: Use connectors](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities): How to add a connected app and switch it on per chat, and how admins can limit write actions.
- [OpenAI: Skills and plugins](https://developers.openai.com/plugins/concepts/skills): The connected app brings live information and actions; the skill brings the workflow around them.
- [Claude Help Centre: Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude): Sharing skills with colleagues and publishing to an organisation library on Team and Enterprise.
- [Anthropic: The complete guide to building skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf): No README inside the skill folder, and naming rules for shared skills.
- [Anthropic: Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview): Use only skills from trusted sources and check every file, because skills can run code.
- [Claude Code docs: Skills](https://code.claude.com/docs/en/skills): Project skills, plugins, allowed-tools and disable-model-invocation.

## Coach notes
Arc: last of five in this topic (write the skill; install it and add an example; test and fix; reference files and templates; connect and get ready to share). Never name the other missions by number to the learner. Levels covered: connect (light) and share (light).
Curriculum boundaries: this topic sits in the no-code Integrating Agents track. Keep connecting to apps the learner already connects to Claude; automations that run on their own belong to the n8n topic, building agents with tools (MCP in depth) to the single-agent prototype topic, permission design to "Scoping permissions and production guardrails", and handover documentation and usage tracking to "Handing off what you built responsibly". Mention them only if the learner asks how to go further.
Levels: guided (A, B) uses a connector they already have (often a drive or calendar), hears "connected app" not MCP, and may use a file export instead; standard (C) chooses the step alone; fast-track (D) uses the claude-code variant with an MCP tool and gets the Go further step (script or by-name-only).
No connector allowed at work: use a file export uploaded with the skill as a stand-in and say plainly that this tests the step, not the live connection. The guard still applies.
Likely errors: a step that says "use the drive" without saying what to read; no line for when the app is unavailable; a guard that says "be careful"; real customer data in the first test; a card that describes how the skill was built instead of how to use and check it; a README inside the folder instead of a card next to it.
Time budget for guided learners (30 minutes in total, profile and level question included): about 4 to 5 minutes per build step. They copy the step's fill-in lines and fill the [blanks]; they never write a part from an empty page. If a step runs over 8 minutes, accept a short version and note one improvement for later. If the connector is not set up, use the file route; connecting an app is not worth 10 minutes of a 30-minute mission.
Feedback: name what is clear (the step, the limit, the card), then the gap, then one fix.
Page state: set the full skill v5 with its guard, version line and card as the part for the last step (Card; Go further for fast-track).
Other vendors: ChatGPT plugins can bundle skills with apps, and workspaces can share and publish skills; Gemini app skills can include scripts that cannot reach external websites, and connect to Google apps. Where equivalence breaks: connector names and permissions differ per tool, so the guard must name the app as the learner sees it.
