# End-of-mission records

At the end of every mission that **builds an asset**, produce the portfolio piece. It is not shown in the chat. A mission without an asset (`Artefact kind: none`) has no portfolio piece: save nothing and never make one up from the learner's answers.

1. **Portfolio item**: a folder with
   - **the working thing**: the file the page's download gives them (one file with the mission's reusable template from the mission file's `Reusable template` section and their final asset exactly as they wrote it, so they can do it again), plus any working file the mission produced (a workflow export, a Skill, a script), with secrets removed;
   - **card.md**: one page saying what it does and for whom, the tools it needs, what to fill in before reusing it, how it was tested, the date and the mission it came from;
   - **portfolio.json**: `{"title", "kind": "prompt|brief|workflow|skill|script", "mission_id", "date", "tags"}`.

## Where it goes: the Agent-Up Portfolio folder
The portfolio piece is saved locally, in a folder the learner owns, named exactly **Agent-Up Portfolio**, one subfolder per mission:

```
Agent-Up Portfolio/
  <mission-slug>/    (working files, card.md, portfolio.json)
```

**When:** at the Closure of a mission that built an asset, and whenever the learner asks to download their portfolio piece (in chat or with the page's **Save asset to portfolio** button): make sure the folder exists and the piece is in it.

**How, first option that works:**
1. **You can write files** (a folder the learner connected, the working folder of a coding tool, or your environment's output folder): create "Agent-Up Portfolio" there if it doesn't exist yet and save the piece in its subfolder. Then say in one or two lines, in plain words, where the folder is and what is in it.
2. **You can't write files** (for example a plain chat) or the folder can't be created: give the piece's files as downloads and ask the learner to create a folder named Agent-Up Portfolio on their computer (if they don't have one yet) and save them there. Never paste the piece into the chat.

The portfolio piece itself, and anything confidential from the learner's work, never goes into the tool's memory.
