#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Load a mission that ships inside this plugin into a scratch folder that mirrors the plugin's layout,
so build.py can read it with --content <scratch>. Prints one JSON line. No network access.
The scratch copy is the coach's working copy: adapting or translating a step never changes the plugin's own files.

  load_mission.py <scratch> --number 2 [--topic <topic-id>] [--lang de]
  load_mission.py <scratch> --list
Exit codes: 0 ok, 2 needs a choice (several topics), 4 mission not found.
"""
import argparse, json, os, re, shutil, sys

SKILL = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
MISSIONS = os.path.join(SKILL, "missions")
TRANSLATIONS = os.path.join(SKILL, "translations")


def title_of(path):
    m = re.search(r"^title:\s*(.+?)\s*$", open(path, encoding="utf-8").read(), re.M)
    return m.group(1).strip("\"'") if m else ""


def out(data, code=0):
    print(json.dumps(data, ensure_ascii=False))
    sys.exit(code)


def copy(rel, scratch):
    src = os.path.join(SKILL, rel)
    dst = os.path.join(scratch, rel)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(src, dst)
    return dst


def catalog():
    """{(topic, number): file name} for every mission file in missions/."""
    found = {}
    if os.path.isdir(MISSIONS):
        for topic in sorted(os.listdir(MISSIONS)):
            tdir = os.path.join(MISSIONS, topic)
            if not os.path.isdir(tdir):
                continue
            for f in sorted(os.listdir(tdir)):
                m = re.match(r"mission-(\d+)-.+\.md$", f)
                if m:
                    found[(topic, int(m.group(1)))] = f
    return found


def main():
    a = argparse.ArgumentParser()
    a.add_argument("scratch")
    a.add_argument("--number", type=int)
    a.add_argument("--topic")
    a.add_argument("--lang", default="en")
    a.add_argument("--list", action="store_true")
    o = a.parse_args()
    found = catalog()
    if o.list:
        rows = []
        for (topic, n), f in sorted(found.items()):
            langs = sorted(l for l in (os.listdir(TRANSLATIONS) if os.path.isdir(TRANSLATIONS) else [])
                           if os.path.exists(os.path.join(TRANSLATIONS, l, topic, f)))
            rows.append({"topic": topic, "number": n, "file": f, "title": title_of(os.path.join(MISSIONS, topic, f)), "translations": langs})
        out({"missions": rows})
    if not o.number:
        out({"error": "usage", "detail": "give --number or --list"}, 4)
    cands = sorted(k for k in found if k[1] == o.number and (not o.topic or k[0] == o.topic))
    if not cands:
        out({"error": "not_found", "detail": "no mission %d%s" % (o.number, " in topic " + o.topic if o.topic else "")}, 4)
    if len(cands) > 1:
        out({"error": "choose_topic", "topics": [c[0] for c in cands]}, 2)
    topic, f = cands[0][0], found[cands[0]]
    en_rel = "missions/%s/%s" % (topic, f)
    mission = copy(en_rel, o.scratch)
    title = title_of(mission)
    topic_rel = "missions/%s/_topic.yaml" % topic
    if os.path.exists(os.path.join(SKILL, topic_rel)):
        copy(topic_rel, o.scratch)
    translated = False
    if o.lang != "en":
        tr_rel = "translations/%s/%s/%s" % (o.lang, topic, f)
        if os.path.exists(os.path.join(SKILL, tr_rel)):
            title = title_of(copy(tr_rel, o.scratch)) or title
            translated = True
            tt = "translations/%s/%s/_topic.yaml" % (o.lang, topic)
            if os.path.exists(os.path.join(SKILL, tt)):
                copy(tt, o.scratch)
    m = re.match(r"mission-(\d+)-", f)
    out({"mission": os.path.abspath(mission), "content": os.path.abspath(o.scratch), "topic": topic,
         "number": int(m.group(1)) if m else None, "file": f, "lang": o.lang, "translated": translated, "title": title})


if __name__ == "__main__":
    main()
