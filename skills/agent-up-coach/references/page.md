# The mission page

The page is a tested template filled straight from the mission file. You never write page content and never rebuild the page after the first build, except when the learner switches language: then fetch the mission again, build once more in the new language, deliver the new file and re-apply their saved parts with `set_state.py`.

## Build (one shell call)
```
cat > <scratch>/example.json <<'EOF'
{"situation": "...", "input": "...", "steps": ["...", "..."], "result": "...", "why": "..."}
EOF
python3 "${CLAUDE_SKILL_DIR}/scripts/build.py" "<mission path printed by fetch_mission.py>" <output folder>/agent-up-<mission stem>.html --content "<content folder printed by fetch_mission.py>" --lang <language code> --learner <name or role slug> --tool <claude-app|claude-code|no-skills> --level <guided|standard|fast-track> --example <scratch>/example.json [--ui <scratch>/ui.json]
```
- `example.json`: the mission's working example adapted to the learner's own work and goals, in the same shape (a real multi-step task, 3-5 steps, no names or data from their real work). Short: about 5 lines. `why` is the mission's Why this matters (Context) retold for that same situation (SKILL.md §5); it replaces the mission file's text on the page. `summary` is 2 to 4 short factual lines about what the mission covered, with the key words in **bold**, for the green box on the closure page (SKILL.md §5); without it the box is not shown. Leave out `--example` to use the mission's own.
- `<output folder>` = where your environment shows files to the learner (in Cowork: the outputs folder).
- `--tool`: `claude-app` (Claude chat, desktop, Cowork; the default, may be left out), `claude-code` (terminal or IDE) or `no-skills`; which one: SKILL.md §6. The mission file may hold `[tool]` variants of sections and steps; the build picks the matching one, else the default.
- `--level`: the learner's level in this topic (SKILL.md §1). The mission file may hold `[level]` variants, for example a `Go further [fast-track]` step.
- `--content`: the `content` folder printed by `fetch_mission.py`: the scratch folder that holds the downloaded `missions/` and `translations/` (and your own translation, if you wrote one).
- `--lang`: the learner's language code. The library's translation is used when `fetch_mission.py` downloaded one; otherwise the English mission, or your own translation (SKILL.md §0). `--ui <scratch>/ui.json` (the page buttons translated by you) only for languages other than en, es and de.
- The command prints `OK` and the page's state keys (`at`, one `part:<step>` per build step). `ERROR` lines mean the mission file is broken or incomplete: say plainly that this mission isn't complete yet, name what is missing in one line and offer another mission; don't patch the mission file. Exception: errors in a translation or an adapted step that you wrote yourself (SKILL.md §0, §1): fix your own text and build again.
- **Delivery, every build, every environment:** deliver the HTML file with your environment's file-delivery tool (e.g. `SendUserFile`) before you say anything about the page. A file written by a script is not delivered by itself.

## Live updates (never rebuild)
```
python3 "${CLAUDE_SKILL_DIR}/scripts/set_state.py" <page.html> <key> "<value>"
```
- `part:<last step>`: the learner's full final portfolio piece, exactly as they wrote it, once the last step is final (and again if the test fixes it). It enables the test's copy button and the **Save portfolio piece** button (one file: the mission's reusable template and the learner's final version). Set only this key and leave the other `part:` keys empty.
- `at`: section.step to reopen at, e.g. `"4.1"`, when you move the learner on.
- Without Python, edit that one line in the `agentup-state` block with your file-edit tool (escape `"` and line breaks).
- The page shows updates when it reloads; if it doesn't refresh by itself, tell the learner to reopen it (their place is kept).
