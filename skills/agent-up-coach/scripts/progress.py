#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Read and update the learner's progress note, progress.json, in their Agent-Up Portfolio folder.
Local files only, no network. The note holds no work content: only language, tool, topic level, and per mission
its title, status and dates.

  progress.py read <folder>
  progress.py set <folder> [--create] [--lang de] [--tool claude-app|claude-code|no-skills]
                [--topic <topic-id> --level guided|standard|fast-track]
                [--topic <topic-id> --mission <mission file name without .md> --title "..." --status started|finished [--portfolio <subfolder>]]
Exit codes: 0 ok, 2 folder missing or not writable, 4 bad arguments.
"""
import argparse, datetime, json, os, sys

NAME = "progress.json"
LEVELS = ("guided", "standard", "fast-track")
STATUS = ("started", "finished")
TOOLS = ("claude-app", "claude-code", "no-skills")


def out(data, code=0):
    print(json.dumps(data, ensure_ascii=False))
    sys.exit(code)


def load(folder, keep_aside=False):
    path = os.path.join(folder, NAME)
    if not os.path.exists(path):
        return {"version": 1, "topics": {}, "missions": {}}, False
    try:
        d = json.load(open(path, encoding="utf-8"))
        if not isinstance(d, dict):
            raise ValueError("not an object")
    except (ValueError, OSError):
        # unreadable note: when writing, keep it aside and start a new one, never lose the learner's file
        if keep_aside:
            os.replace(path, path + ".bak")
        return {"version": 1, "topics": {}, "missions": {}}, False
    d.setdefault("version", 1)
    d.setdefault("topics", {})
    d.setdefault("missions", {})
    return d, True


def write(folder, d):
    path = os.path.join(folder, NAME)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
        f.write("\n")
    os.replace(tmp, path)


def main():
    a = argparse.ArgumentParser()
    a.add_argument("cmd", choices=("read", "set"))
    a.add_argument("folder")
    a.add_argument("--create", action="store_true", help="create the folder (not its parents) if it does not exist")
    a.add_argument("--lang")
    a.add_argument("--tool", choices=TOOLS)
    a.add_argument("--topic")
    a.add_argument("--level", choices=LEVELS)
    a.add_argument("--mission")
    a.add_argument("--title")
    a.add_argument("--status", choices=STATUS)
    a.add_argument("--portfolio")
    a.add_argument("--date", help="YYYY-MM-DD, default today")
    o = a.parse_args()
    folder = os.path.abspath(o.folder)
    if o.cmd == "read":
        if not os.path.isdir(folder):
            out({"exists": False, "folder": False, "topics": {}, "missions": {}})
        d, exists = load(folder)
        d["exists"] = exists
        d["folder"] = True
        out(d)
    if (o.level and not o.topic) or (o.status and not (o.topic and o.mission)):
        out({"error": "usage", "detail": "--level needs --topic, and --status needs --topic and --mission"}, 4)
    try:
        if o.create and not os.path.isdir(folder):
            os.mkdir(folder)
        if not os.path.isdir(folder):
            out({"error": "no_folder", "detail": "the folder does not exist"}, 2)
        d, _ = load(folder, keep_aside=True)
        today = o.date or datetime.date.today().isoformat()
        if o.lang:
            d["language"] = o.lang
        if o.tool:
            d["tool"] = o.tool
        if o.topic and o.level:
            d["topics"].setdefault(o.topic, {})["level"] = o.level
        if o.topic and o.mission and o.status:
            key = "%s/%s" % (o.topic, o.mission)
            m = d["missions"].setdefault(key, {})
            if o.title:
                m["title"] = o.title
            if o.portfolio:
                m["portfolio"] = o.portfolio
            m.setdefault("started", today)
            if o.status == "finished":
                m["status"] = "finished"
                m["finished"] = today
            elif m.get("status") != "finished":
                # starting a mission again never undoes a finished one
                m["status"] = "started"
        d["updated"] = today
        write(folder, d)
    except OSError as e:
        out({"error": "write_failed", "detail": str(e)}, 2)
    d["exists"] = True
    out(d)


if __name__ == "__main__":
    main()
