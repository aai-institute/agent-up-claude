# End-of-mission records

At the end of every mission that **builds a portfolio piece**, save it. It is not shown in the chat. A mission without one (`Artefact kind: none`): save nothing and never make one up from the learner's answers.

1. **Portfolio item**: a folder with
   - **the working thing**: the learner's final file, named like the draft you delivered (for a skill: `<skill name>-v1.md`, the `Artefact file` with `my-skill` replaced by the skill's name), exactly as they wrote it, plus a second file `<skill name>-v1-portfolio.md` with the mission's reusable template (from the `Reusable template` section) first and their final version after it, so they can do it again. This second file has the same name and content as the page's **Save portfolio piece** download. Add any other working file the mission produced (a workflow export, a script), with secrets removed;
   - **card.md**: one page saying what it does and for whom, the tools it needs, what to fill in before reusing it, how it was tested, the date and the mission it came from;
   - **portfolio.json**: `{"title", "kind": "prompt|brief|workflow|skill|script", "mission_id", "date", "tags"}`.

## Where it goes: the Agent-Up Portfolio folder
The portfolio piece is saved locally, in a folder the learner owns, named exactly **Agent-Up Portfolio**, one subfolder per mission, named like the mission file without `.md` (the `file` that `load_mission.py` printed, for example `01-create-your-first-skill`). Use that same name for `--portfolio` in `progress.md`:

```
Agent-Up Portfolio/
  <mission-file-name>/    (working files, card.md, portfolio.json)
```

**When:** at the Closure of a mission that built a portfolio piece, and whenever the learner asks to download their portfolio piece (in chat or with the page's **Save portfolio piece** button): make sure the folder exists and the piece is in it. The page's **Save portfolio piece** button gives a copy in the browser's Downloads; that is fine, the folder copy is the one that counts.

**How, first option that works:**
1. **You can write files** (a folder the learner connected, the working folder of a coding tool, or your environment's output folder): use the Agent-Up Portfolio folder there (set up as `progress.md` describes; create it only if the learner agreed to it) and save the piece in its subfolder. Then say in one or two lines, in plain words, where the folder is and what is in it.
2. **You can't write files** (for example a plain chat) or the folder can't be created: give the piece's files as downloads and ask the learner to create a folder named Agent-Up Portfolio on their computer (if they don't have one yet) and save them there. Never paste the piece into the chat.

The portfolio piece itself, and anything confidential from the learner's work, never goes into the tool's memory.
