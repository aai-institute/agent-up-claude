#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Fetch a mission from the public Agent Up content library into a scratch folder that mirrors the library layout,
so build.py can read it with --content <scratch>. Prints one JSON line. The coach never writes this content.

  fetch_mission.py <scratch> --link <link to a mission file> [--lang de]
  fetch_mission.py <scratch> --number 2 [--topic <topic-id>] [--lang de]
  fetch_mission.py <scratch> --list
Exit codes: 0 ok, 2 needs a choice (several topics), 3 network error, 4 mission not found.
"""
import argparse, json, os, re, sys, urllib.error, urllib.parse, urllib.request

REPO = "aai-institute/agentup-content-library"
BRANCH = "main"
RAW = "https://raw.githubusercontent.com/%s/%s/" % (REPO, BRANCH)
TREE = "https://api.github.com/repos/%s/git/trees/%s?recursive=1" % (REPO, BRANCH)


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "agent-up-coach"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read()


def tree():
    return {t["path"] for t in json.loads(get(TREE)).get("tree", []) if t.get("type") == "blob"}


def fetch(path):
    return get(RAW + urllib.parse.quote(path)).decode("utf-8")


def save(scratch, path, text):
    f = os.path.join(scratch, path)
    os.makedirs(os.path.dirname(f), exist_ok=True)
    open(f, "w", encoding="utf-8").write(text)
    return f


def title_of(text):
    m = re.search(r"^title:\s*(.+?)\s*$", text, re.M)
    return m.group(1).strip("\"'") if m else ""


def out(data, code=0):
    print(json.dumps(data, ensure_ascii=False))
    sys.exit(code)


def from_link(link):
    m = re.search(r"github\.com/%s/blob/[^/]+/(.+?)(?:[?#].*)?$" % re.escape(REPO), link) or \
        re.search(r"raw\.githubusercontent\.com/%s/[^/]+/(.+?)(?:[?#].*)?$" % re.escape(REPO), link)
    if not m:
        return None
    path = urllib.parse.unquote(m.group(1))
    t = re.match(r"translations/([^/]+)/([^/]+)/(mission-[^/]+\.md)$", path)
    if t:
        return t.group(1), t.group(2), t.group(3)
    e = re.match(r"missions/([^/]+)/(mission-[^/]+\.md)$", path)
    return ("en", e.group(1), e.group(2)) if e else None


def main():
    a = argparse.ArgumentParser()
    a.add_argument("scratch")
    a.add_argument("--link")
    a.add_argument("--number", type=int)
    a.add_argument("--topic")
    a.add_argument("--lang", default="en")
    a.add_argument("--list", action="store_true")
    o = a.parse_args()
    try:
        paths = tree()
        found = {}
        for p in paths:
            m = re.match(r"missions/([^/]+)/(mission-(\d+)-[^/]+\.md)$", p)
            if m:
                found[(m.group(1), int(m.group(3)))] = m.group(2)
        if o.list:
            rows = []
            for (topic, n), f in sorted(found.items()):
                langs = sorted(p.split("/")[1] for p in paths if re.match(r"translations/[^/]+/%s/%s$" % (re.escape(topic), re.escape(f)), p))
                rows.append({"topic": topic, "number": n, "file": f, "title": title_of(fetch("missions/%s/%s" % (topic, f))), "translations": langs})
            out({"missions": rows})
        lang = o.lang
        if o.link:
            parsed = from_link(o.link)
            if not parsed:
                out({"error": "not_found", "detail": "that is not a link to a mission file of the Agent Up content library"}, 4)
            link_lang, topic, f = parsed
            if link_lang != "en" and lang == "en":
                lang = link_lang
        elif o.number:
            cands = sorted(k for k in found if k[1] == o.number and (not o.topic or k[0] == o.topic))
            if not cands:
                out({"error": "not_found", "detail": "no mission %d%s" % (o.number, " in topic " + o.topic if o.topic else "")}, 4)
            if len(cands) > 1:
                out({"error": "choose_topic", "topics": [c[0] for c in cands]}, 2)
            topic, f = cands[0][0], found[cands[0]]
        else:
            out({"error": "usage", "detail": "give --link, --number or --list"}, 4)
        en_path = "missions/%s/%s" % (topic, f)
        if en_path not in paths:
            out({"error": "not_found", "detail": en_path + " does not exist in the library"}, 4)
        text = fetch(en_path)
        mission = save(o.scratch, en_path, text)
        title = title_of(text)
        topic_file = "missions/%s/_topic.yaml" % topic
        if topic_file in paths:
            save(o.scratch, topic_file, fetch(topic_file))
        translated = False
        if lang != "en":
            tp = "translations/%s/%s/%s" % (lang, topic, f)
            if tp in paths:
                ttext = fetch(tp)
                save(o.scratch, tp, ttext)
                title = title_of(ttext) or title
                translated = True
                tt = "translations/%s/%s/_topic.yaml" % (lang, topic)
                if tt in paths:
                    save(o.scratch, tt, fetch(tt))
        m = re.match(r"mission-(\d+)-", f)
        out({"mission": os.path.abspath(mission), "content": os.path.abspath(o.scratch), "topic": topic,
             "number": int(m.group(1)) if m else None, "file": f, "lang": lang, "translated": translated, "title": title})
    except (urllib.error.URLError, OSError, ValueError) as e:
        out({"error": "network", "detail": str(e)}, 3)


if __name__ == "__main__":
    main()
