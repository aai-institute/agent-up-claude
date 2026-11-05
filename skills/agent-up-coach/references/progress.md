# The Agent-Up Portfolio folder and progress

The learner keeps one folder on their computer, named exactly **Agent-Up Portfolio**. It does two things: it holds the portfolio pieces they build (one subfolder per mission, see `saving.md`), and it holds a small progress note, `progress.json`, so that a new chat knows which missions they have started or finished and doesn't ask again what it already knows. Nothing else is saved there, and it never leaves their computer. The portfolio piece, the learner's real work and anything confidential never go into the note.

Read this at the start of first contact (§1). Steps 1 and 2 come before the mini form, step 3 after the mini form and before the page is built, step 4 as marked, and again at Closure.

## 1. Look for the folder (silently, every new chat)
Check whether you can read and write files: a folder the learner connected, the working folder of a coding tool, or your environment's output folder. If you can't (a plain chat), skip this whole file: never mention the folder, give portfolio pieces as downloads (`saving.md`), and carry on as usual.

Otherwise look for a folder named **Agent-Up Portfolio**: the connected or working folder itself (check its own name first), or a subfolder of it. If you find it, `<portfolio>` is its full path (the connected folder itself when it is named that, otherwise `<connected folder>/Agent-Up Portfolio`). Run
`python3 "${CLAUDE_SKILL_DIR}/scripts/progress.py" read "<the folder>"`
It prints one JSON line: `exists` (a progress note is there), `language`, `tool`, `topics` (`level` per topic id) and `missions` (key `<topic>/<mission file name>`, with `title`, `status` `started` or `finished`, `started`, `finished`, `portfolio`).

## 2. Welcome the learner back (when the note exists)
- Your welcome at the start of the chat comes before these tool calls, so keep it short and neutral; this welcome-back line follows it.
- Say in one or two sentences, in their language, which missions they finished (by title) and offer the next one, in any order. Never list dates or statuses as a table.
- Use what it holds: the language, the tool (`claude-app` is answer A of the mini form, `claude-code` is B) and the level of a topic you have seen before. Skip those questions. You still ask for their work and goal, because that isn't saved.
- If the opening message names a mission they already finished, say so in one line and go on with it. Nothing is lost: the first version stays in their portfolio folder.
- If this mission needs a skill from an earlier one (the mission file says so), ask whether they still have the skill or file they built before (don't name the other mission).
- If the mission shows `started` but not `finished`, say that they began it on that date and that you start it again from the beginning, because the page of the earlier chat isn't kept.

## 3. Offer to set the folder up (when there is no Agent-Up Portfolio folder yet)
Ask once, before building the page, in the learner's language, with the reason first. Close to this wording: "I'd like to keep a folder named Agent-Up Portfolio for you. It holds the portfolio pieces you build, so you keep them, and a small note of which missions you have done, so a new chat picks up where you stopped and doesn't ask the same things again. It stays on your computer and holds nothing else. Shall I set it up?"
- **No** → say fine in one line, never ask again in this chat, and carry on without a folder: the portfolio piece is given as a download at the end.
- **Yes** → one action at a time, and wait for their answer after each:
  1. Your environment may let you ask for access to a folder. If it does, ask for it, so the learner only has to accept the request. If a folder is already connected, say nothing about "Add folder": create **Agent-Up Portfolio** inside it yourself, with `progress.py set "<portfolio>" --create ...` (step 3 below). If the shell can't see the connected folder, treat it as "can't write files".
  2. If you can't ask, tell them the one step that fits their environment. In the Claude desktop app: "Click **Add folder**, create a new folder called Agent-Up Portfolio, for example in your Documents, and select it. You approve access once." In Claude Code: "Start me from a folder you keep for this, and approve the access when asked; I create Agent-Up Portfolio in it."
  3. When they say it is done, create the note: `python3 "${CLAUDE_SKILL_DIR}/scripts/progress.py" set "<portfolio>" --create --lang <code> --tool <claude-app|claude-code|no-skills>` and tell them in one line that the folder is ready.
- If anything fails, say so in one line, carry on without a folder and never block the mission.

## 4. Keep the note up to date
Always with the script, never by writing the file yourself. Run each command in the same shell call as the step it belongs to.
- **Mission starts** (profile and level known, when you build the page; if the folder was just agreed, this one command may carry `--create` too): `progress.py set "<portfolio>" --lang <code> --tool <claude-app|claude-code|no-skills> --topic <topic-id> --level <guided|standard|fast-track> --mission "<mission file name without .md>" --title "<mission title>" --status started`
- **Closure** (the mission is over): the same command with `--status finished`, and `--portfolio "<mission subfolder name>"` when the mission built a portfolio piece. Do this even when the mission built no portfolio piece.
- The mission file name and topic id are the `file` and `topic` that `load_mission.py` printed (without `.md`).
- If a command fails, don't retry more than once and don't tell the learner more than one line.
- At Closure, when the folder is set up, remind them in one line that in their next chat they connect the same folder first, so Agent Up sees their progress.
