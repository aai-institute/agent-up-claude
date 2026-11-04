# agent-up-claude

Claude plugin for **Agent Up**, appliedAI's program for becoming agent-native. It adds one skill, `agent-up-coach`, that runs one hands-on mission of 20-30 minutes at a time: it coaches the learner in the chat and builds a personal mission page that opens next to the chat.

The missions are not part of this plugin. They live in the public [Agent Up content library](https://github.com/aai-institute/agentup-content-library), and the coach fetches the mission fresh every time, because the library is updated every week.

## Install

**Claude (chat and Cowork):** download `agent-up-claude.zip` from the Agent Up website or from the [latest release on GitHub](https://github.com/aai-institute/agent-up-claude/releases/latest), then in Claude open Settings, Plugins, and add the ZIP.

**Claude Code:**

```
/plugin marketplace add aai-institute/agent-up-claude
/plugin install agent-up-coach@agent-up-claude-marketplace
```

## Starting a mission

1. On the Agent Up website the learner copies the mission prompt. It holds a link to the mission file in the content library.
2. The learner pastes it into a new Claude chat. Typing "Start mission 2" also works, and missions can be done in any order.
3. The coach downloads the mission, asks one short mini form (work and goal, Claude chat / Cowork or terminal / Claude Code, and the topic level), adapts the working example to the learner's work, builds the mission page and coaches in the chat.
4. At the end, if the mission built a portfolio piece, the learner saves it to their portfolio (one file with the mission's reusable template and their own final version) and goes back to the Agent Up website.

All missions should be done in the same chat, because a new chat starts without memory of the earlier ones. The coach answers in the learner's language: it uses the library's translation when there is one, and translates the mission itself when there is not.

If Claude cannot reach GitHub, the coach asks the learner for permission to use a web tool, or shows how to copy the mission text by hand.

## Structure

```
.claude-plugin/
├── plugin.json
└── marketplace.json
skills/
└── agent-up-coach/
    ├── SKILL.md                # the coach: first contact, chat rules, pedagogy, mission shape, end of mission
    ├── references/
    │   ├── page.md             # how to build and update the mission page
    │   └── saving.md           # end of mission: the portfolio piece and the Agent-Up Portfolio folder
    ├── assets/
    │   ├── lesson-template.html   # the mission page (interface texts for English, Spanish and German built in)
    │   └── brand/                 # the two logos used by the page
    └── scripts/
        ├── fetch_mission.py    # downloads a mission from the content library
        ├── build.py            # mission file to mission page; --dump-ui and --ui for other languages
        └── set_state.py        # small live updates to the page (final portfolio piece, position)
```

## Version 1.0.0

First public release.

- The plugin is `agent-up-coach` in the marketplace `agent-up-claude-marketplace` and works with Claude only.
- Missions and translations are not in the plugin: `fetch_mission.py` downloads them from the content library, by link, by mission number or by listing the topics.
- Any language: the library's translation is used when it exists, otherwise the coach translates the mission, and the page's buttons and labels are translated through `build.py --dump-ui` and `--ui`.
- First contact is a short mini form, and the coach adapts the examples, wording and steps to the learner's work and environment without changing what the mission teaches.
- The mission page ends with a short summary of the mission, a **Save portfolio piece** button and a button back to the Agent Up website. Missions that build nothing to keep have no save button and only the back button. The coach also saves the piece (the file, a working file if any, `card.md` and `portfolio.json`) in a local folder named Agent-Up Portfolio when it can write files.

## Configuration

By default the "Back to Agent Up Website" button opens the Agent Up website. Set the environment variable `AGENTUP_SITE_URL` when building a page to point it to another address, for example a local test site.

## License

The text and instructions are licensed under [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/), like the content library. The code (the scripts and the page template) is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0). The logos are trademarks of the appliedAI Institute for Europe gGmbH and are not licensed for reuse. See [LICENSE](LICENSE) and the folder `LICENSES/`.
