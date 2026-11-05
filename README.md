# agent-up-claude

Claude plugin for **Agent Up**, appliedAI's program for becoming agent-native. It adds one skill, `agent-up-coach`, that runs one hands-on mission of 20-30 minutes at a time: it coaches the learner in the chat and builds a personal mission page that opens next to the chat.

The missions are part of this plugin: they ship inside it, in English and German, so the coach starts a mission without connecting to anything. A change to a mission is a new plugin release.

## Install

**Claude (chat and Cowork):** download `agent-up-claude.zip` from the Agent Up website or from the [latest release on GitHub](https://github.com/aai-institute/agent-up-claude/releases/latest), then in Claude open Settings, Plugins, and add the ZIP.

**Claude Code:**

```
/plugin marketplace add aai-institute/agent-up-claude
/plugin install agent-up-coach@agent-up-claude-marketplace
```

## Starting a mission

1. On the Agent Up website the learner copies the mission prompt. It names the skill, the topic, the mission and the language, for example: *Use the agent-up-coach skill to start Agent Up mission 1, "Write your first skill", from the topic "Authoring Reusable Skills" (authoring-reusable-skills). Answer in English.*
2. The learner pastes it into a new Claude chat. Typing "Start mission 2" also works, and missions can be done in any order.
3. The coach loads the mission from the plugin, asks one short mini form (work and goal, Claude chat / Cowork or terminal / Claude Code, and the topic level), adapts the working example to the learner's work, builds the mission page and coaches in the chat.
4. At the end, if the mission built a portfolio piece, the learner saves it to their portfolio (one file with the mission's reusable template and their own final version) and goes back to the Agent Up website.

All missions should be done in the same chat, because a new chat starts without memory of the earlier ones. The coach answers in the learner's language: it uses the translation in the plugin when there is one, and translates the mission itself when there is not.

## Structure

```
.claude-plugin/
├── plugin.json
└── marketplace.json
skills/
└── agent-up-coach/
    ├── SKILL.md                # the coach: first contact, chat rules, pedagogy, mission shape, end of mission
    ├── missions/               # the missions in English: one folder per topic (_topic.yaml + mission-<n>-<slug>.md)
    ├── translations/           # <lang>/<topic>/: the same missions in German
    ├── references/
    │   ├── page.md             # how to build and update the mission page
    │   └── saving.md           # end of mission: the portfolio piece and the Agent-Up Portfolio folder
    ├── assets/
    │   ├── lesson-template.html   # the mission page (interface texts for English, Spanish and German built in)
    │   └── brand/                 # the two logos used by the page
    └── scripts/
        ├── load_mission.py     # copies a mission from the plugin into a scratch folder, by topic, number and language, or lists them
        ├── build.py            # mission file to mission page; --dump-ui and --ui for other languages
        └── set_state.py        # small live updates to the page (final portfolio piece, position)
```

## Version 1.0.1

The missions now ship inside the plugin. Nothing is downloaded when a mission starts.

- `missions/` (English) and `translations/de/` (German) hold the topic "Authoring Reusable Skills": 5 missions each, with their `_topic.yaml`, exactly as in the Learning Engine plugin v11.2.
- `load_mission.py` replaces `fetch_mission.py`. It copies a mission from the plugin into a scratch folder, so adapting or translating a step never changes the plugin's own files.
- The mission prompt on the website names the skill, the topic, the mission and the language. It has no link.
- Users who add the plugin from the marketplace get the missions with the update.

## Version 1.0.0

First public release.

- The plugin is `agent-up-coach` in the marketplace `agent-up-claude-marketplace` and works with Claude only.
- Missions and translations were downloaded when a mission started (replaced in 1.0.1, see above).
- Any language: a translation is used when there is one, otherwise the coach translates the mission, and the page's buttons and labels are translated through `build.py --dump-ui` and `--ui`.
- First contact is a short mini form, and the coach adapts the examples, wording and steps to the learner's work and environment without changing what the mission teaches.
- The mission page ends with a short summary of the mission, a **Save portfolio piece** button and a button back to the Agent Up website. Missions that build nothing to keep have no save button and only the back button. The coach also saves the piece (the file, a working file if any, `card.md` and `portfolio.json`) in a local folder named Agent-Up Portfolio when it can write files.

## Configuration

By default the "Back to Agent Up Website" button opens the Agent Up website, <https://aai-institute.github.io/frontier-ai-academy/>. Set the environment variable `AGENTUP_SITE_URL` when building a page to point it to another address, for example a local test site.

## License

This repository has three parts, each with its own license. The file [LICENSE](LICENSE) lists which files belong to which part, and the full license texts are in the folder `LICENSES/`.

**Text, instructions and missions: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)** (Creative Commons Attribution-ShareAlike 4.0 International). This covers `SKILL.md`, the files in `references/`, the missions in `missions/`, their translations in `translations/` and this README. You may use, copy, share and adapt them, also for commercial purposes, if you:

- give credit to the appliedAI Institute for Europe gGmbH, link to the license and say if you changed anything;
- share your adapted version under the same license (CC BY-SA 4.0, or a license Creative Commons lists as compatible).

**Code: [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).** This covers the scripts in `scripts/` and the page template `assets/lesson-template.html`. You may use, modify and distribute them, also for commercial purposes, if you keep the copyright and license notices and mark the files you changed. The license includes a patent grant and no warranty.

**Logos: not licensed.** The images in `assets/brand/` are trademarks of the appliedAI Institute for Europe gGmbH. Neither license above covers them, and they may not be reused without permission.

This is a summary and not legal advice. If it differs from the license texts, the license texts apply.
