#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Build an Agent Up lesson page straight from a lesson .md. The coach writes no content.

  build.py missions/<topic>/<lesson.md> <out.html> [--lang de] [--learner x] [--example ex.json]   build the page (a few ms)
  build.py missions/<topic>/<lesson.md> --check                                 author-time checks only (every tool variant)
With --tool, sections and steps whose heading ends in [<tool>] (or [<tool>, <tool>]) replace the untagged ones for that tool:
`## Test [claude-code]` replaces `## Test`, `### Install [chatgpt, gemini]` replaces `### Install`. A step that exists only
with tags is left out for the other tools. Tools: claude-app (default), claude-code, chatgpt, gemini, no-skills.
With --level, [guided], [standard] or [fast-track] tags work the same way (e.g. `### Go further [fast-track]`).
With --lang, translations/<lang>/<topic>/<same file name> is used when it exists (page UI in en, es or de):
its frontmatter texts replace the English ones, and its sections replace the English page when it has any.
With --content <folder>, missions/ and translations/ are read from that folder (same layout as the skill folder) instead of
the skill folder: the coach copies the mission files there with load_mission.py. With --ui <file.json>, its texts replace the page's built-in
interface texts, so the page can be shown in any language. --dump-ui prints the English interface texts as JSON (the list to translate).
"""
import sys, re, json, os, base64, time, argparse, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(HERE)
MISSIONS = os.path.join(SKILL, "missions")
CONTENT = SKILL
FRONTMATTER = re.compile(r"\A\ufeff?---\r?\n(.*?)\r?\n---\r?\n?", re.S)
REQUIRED = ("id", "number", "title", "summary", "artefact")
TRANSLATED = ("title", "summary", "artefact")
DASH = re.compile("[–—]")
TOOLS = ("claude-app", "claude-code", "chatgpt", "gemini", "no-skills")
LEVELS = ("guided", "standard", "fast-track")
TAG = re.compile(r"^(.*?)\s*\[([a-z, -]+)\]\s*$")
UMLAUT = str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss", "é": "e", "è": "e", "à": "a", "ñ": "n"})
PREV = re.compile(r"\b(mission|missions) \d", re.I)
CLAIMS = re.compile(r"\b(you have learned|you've learned|now you (know|understand)|you (have )?mastered)\b", re.I)


def scalar(v):
    if v[:1] == '"':
        return json.loads(v)
    if v[:1] == "'":
        return v[1:-1].replace("''", "'")
    return {"true": True, "false": False}.get(v, int(v) if v.isdigit() else v)


def frontmatter(text):
    """The leading --- block of one-line `key: value` pairs, and the text after it."""
    m = FRONTMATTER.match(text)
    if not m:
        return {}, text
    fm = {}
    for l in m.group(1).splitlines():
        if l.strip() and not l.lstrip().startswith("#"):
            k, _, v = l.partition(":")
            fm[k.strip()] = scalar(v.strip())
    return fm, text[m.end():]


def topic_texts(folder):
    f = os.path.join(folder, "_topic.yaml")
    return frontmatter("---\n" + open(f, encoding="utf-8").read().strip() + "\n---\n")[0] if os.path.exists(f) else {}


def translated(path, lang):
    return os.path.join(CONTENT, "translations", lang, os.path.relpath(os.path.abspath(path), MISSIONS))


def sections(md):
    parts = re.split(r"^## +(.+?)\s*$", md, flags=re.M)
    return parts[0], {k.strip(): v.strip() for k, v in zip(parts[1::2], parts[2::2])}


def kv(txt, key):
    m = re.search(r"^" + re.escape(key) + r":[ \t]*(.+)$", txt or "", re.M)
    return m.group(1).strip() if m else ""


def bullets(txt):
    return [l[2:].strip() for l in (txt or "").splitlines() if l.startswith("- ")]


def pair(item):
    a, _, b = item.partition(": ")
    return {"label": a.strip(), "text": b.strip()}


def fence_after(txt, key):
    m = re.search(r"^" + key + r":\s*\n```[^\n]*\n(.*?)^```", txt or "", re.M | re.S)
    return m.group(1).rstrip() if m else ""


def numbered(txt, key):
    m = re.search(r"^" + key + r":[ \t]*\n((?:\d+\. .+\n?)+)", txt or "", re.M)
    return [re.sub(r"^\d+\. ", "", l).strip() for l in m.group(1).splitlines() if l.strip()] if m else []


def tags(name):
    """'Install [chatgpt, gemini]' -> ('Install', ['chatgpt', 'gemini']); untagged -> (name, [])."""
    m = TAG.match(name)
    return (m.group(1).strip(), [x.strip() for x in m.group(2).split(",")]) if m else (name.strip(), [])


def pick(pairs, tool, level="guided"):
    """From (heading, text) pairs keep one per base heading, in first-seen order: the [tool] or [level] version, else the untagged one."""
    order, chosen = [], {}
    for name, text in pairs:
        base, tl = tags(name)
        if base not in order:
            order.append(base)
        if (tool in tl or level in tl) or (not tl and base not in chosen):
            chosen[base] = (text, bool(tl))
    return [(b, chosen[b][0]) for b in order if b in chosen]


def variant_tags(md):
    return {t for h in re.findall(r"^#{2,3} +(.+?)\s*$", md, re.M) for t in tags(h)[1]}


def parse(path, lang="en", tool="claude-app", level="guided"):
    md = open(path, encoding="utf-8").read()
    fm, body = frontmatter(md)
    topic = topic_texts(os.path.dirname(os.path.abspath(path)))
    loc = translated(path, lang)
    if lang != "en" and os.path.exists(loc):
        md = open(loc, encoding="utf-8").read()
        tfm, tbody = frontmatter(md)
        fm.update({k: v for k, v in tfm.items() if k in TRANSLATED and v})
        body = tbody if sections(tbody)[1] else body
        topic.update({k: v for k, v in topic_texts(os.path.dirname(loc)).items() if v})
    head, S = sections(body)
    S = dict(pick(S.items(), tool, level))
    d = {"fm": fm, "title": str(fm.get("title", "")), "website": " ".join(str(fm.get("summary", "")).split())}
    d["meta"] = {k: kv(head, n) for k, n in [("track", "Track"), ("level", "Level"),
                 ("time", "Time"), ("tools", "Tools"), ("kind", "Artefact kind"), ("file", "Artefact file")]}
    d["meta"].update(topic=str(topic.get("title", "")), topic_description=str(topic.get("description", "")), lesson=str(fm.get("number", "")), artefact=str(fm.get("artefact", "")))
    d["context"], d["task"], d["outcome"] = S.get("Context", ""), S.get("Your task", ""), S.get("After this, you can", "")
    d["need"], d["already"] = bullets(S.get("You need")), bullets(S.get("You should already"))
    c = S.get("Concept", "")
    d["concept"] = {"heading": kv(c, "Heading"), "lead": kv(c, "Lead"), "close": kv(c, "Close"), "cards": [pair(b) for b in bullets(c)]}
    d["concept"]["toggles"] = [{"q": m.group(1).strip(), "a": m.group(2).strip()} for m in re.finditer(r"^Toggle: (.+?) \| (.+)$", c, re.M)]
    q = S.get("Check your understanding", "")
    if q:
        d["concept"]["check"] = {"question": kv(q, "Question"), "options": [pair(b) for b in bullets(q)], "answer": kv(q, "Answer"), "why": kv(q, "Why")}
    im = kv(c, "Image")
    if im:
        src, _, alt = im.partition("|")
        f = os.path.join(SKILL, "assets", src.strip())
        if os.path.exists(f):
            mime = {"svg": "image/svg+xml", "png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg", "webp": "image/webp"}[f.rsplit(".", 1)[-1].lower()]
            d["concept"]["image"] = {"src": "data:%s;base64,%s" % (mime, base64.b64encode(open(f, "rb").read()).decode()), "alt": alt.strip()}
        else:
            d.setdefault("_warn", []).append("image not found, left out: " + src.strip())
    cp = S.get("Compare", "")
    if cp:
        d["compare"] = {"bad": fence_after(cp, "Bad"), "good": fence_after(cp, "Good"), "ask": kv(cp, "Ask")}
    w = S.get("Working example", "")
    d["scenario"] = {"situation": kv(w, "Situation"), "input": kv(w, "Input"), "steps": bullets(w), "result": kv(w, "Result"), "ask": kv(w, "Ask")} if w else None
    d["steps"] = [{"name": n.strip(), "use": kv(b, "Use"), "why": kv(b, "Why"), "do": kv(b, "Do"), "instructions": numbered(b, "Do"), "ask": kv(b, "Ask"), "code": fence_after(b, "Code"),
                   "example": {"good": fence_after(b, "Example"), "bad": fence_after(b, "Weak")}}
                  for n, b in pick(zip(*[iter(re.split(r"^### +(.+?)\s*$", S.get("Steps", ""), flags=re.M)[1:])] * 2), tool, level)]
    t = S.get("Test", "")
    d["test"] = {"privacy": kv(t, "Privacy"), "do": kv(t, "Do"), "instructions": numbered(t, "Do"), "checks": bullets(t), "ask": kv(t, "Ask")}
    d["other"] = [pair(b) for b in bullets(S.get("Other ways") or S.get("Other tools"))]
    d["done"], d["practice"] = bullets(S.get("Done when")), bullets(S.get("Practice"))
    tr = S.get("Trust check", "")
    laws = [{"name": m.group(1), "says": m.group(2), "source": m.group(3), "url": m.group(4)} for m in
            re.finditer(r"^- (.+?): (.*?)\s*\[(.+?)\]\((https?://\S+?)\)\s*$", tr, re.M)]
    names, watch = [l["name"] for l in laws], []
    for b in bullets(tr.split("Rules:")[0]):
        m = re.search(r"\s*\(([^()]+)\)$", b)
        if "](" not in b:
            watch.append({"text": b[:m.start()] if m and m.group(1) in names else b, "rule": m.group(1) if m and m.group(1) in names else ""})
    d["trust"] = {"watch": watch, "laws": laws, "ask": kv(tr, "Ask")}
    rt = S.get("Reusable template", "")
    if rt:
        m = re.search(r"^```[^\n]*\n(.*?)^```", rt, re.M | re.S)
        d["template"] = {"name": kv(rt, "Name"), "text": m.group(1).rstrip() if m else ""}
    d["glossary"] = [pair(b) for b in bullets(S.get("Glossary"))]
    d["sources"] = [{"title": m.group(1), "url": m.group(2), "value": m.group(3) or ""} for m in
                    re.finditer(r"^- \[(.+?)\]\((https?://[^)\s]+)\)(?:: (.+))?$", S.get("Sources", ""), re.M)]
    return md, d


def check(path, md, d):
    e, w = [], list(d.pop("_warn", []))
    fm = d.pop("fm")
    folder = os.path.dirname(os.path.abspath(path))
    if os.path.dirname(folder) != MISSIONS:
        e.append("the mission file must be in a topic folder, missions/<topic>/ (inside the --content folder)")
    elif not d["meta"]["topic"]:
        e.append("missing title in " + os.path.join(os.path.basename(folder), "_topic.yaml"))
    missing = [k for k in REQUIRED if fm.get(k) in (None, "")]
    if missing:
        e.append("frontmatter is missing " + ", ".join(missing))
    if fm.get("id") and not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", str(fm["id"])):
        e.append("frontmatter id: lowercase letters, digits and dashes only")
    if fm.get("number") not in (None, "") and (not isinstance(fm["number"], int) or isinstance(fm["number"], bool) or fm["number"] < 1):
        e.append("frontmatter number: a whole number from 1")
    if "published" in fm and not isinstance(fm["published"], bool):
        e.append("frontmatter published: true or false")
    learner_part = md.split("## Coach notes")[0].splitlines()
    for i, l in enumerate(md.splitlines(), 1):
        if i <= len(learner_part) and re.search(r"\blessons?\b", l, re.I):
            e.append("line %d: say 'mission' to the learner, not 'lesson'" % i)
        if DASH.search(l):
            e.append("line %d: em/en dash" % i)
        if i <= len(learner_part) and PREV.search(l):
            e.append("line %d: don't point to other missions by number (%s): name the thing itself" % (i, PREV.search(l).group(0)))
        if CLAIMS.search(l):
            e.append("line %d: claims learning (%s)" % (i, CLAIMS.search(l).group(0)))
    if len(d["title"]) > 48:
        e.append("title over 48 characters")
    if not d["meta"]["topic_description"]:
        e.append("missing description in _topic.yaml (from the curriculum, for the website)")
    if len(d["meta"]["topic_description"]) > 200:
        e.append("topic description in _topic.yaml: max 200 characters")
    if d["website"] and (len(d["website"]) > 200 or "**" in d["website"] or "[[" in d["website"]):
        e.append("frontmatter summary: plain text, max 200 characters")
    for k in ("context", "task", "outcome"):
        if not d[k]:
            e.append("missing section for " + k)
    if not d["steps"] or any(not (s["do"] or s["instructions"]) for s in d["steps"]):
        e.append("every step needs Do: (one line, or a numbered list of instructions)")
    if not (d["test"]["do"] or d["test"]["instructions"]):
        e.append("Test needs Do: (one line, or a numbered list of instructions)")
    if any(not s["instructions"] and not s["ask"] for s in d["steps"]):
        e.append("a one-line Do: is a task for the chat, so it needs Ask:")
    if not 1 <= len(d["trust"]["watch"]) <= 3:
        e.append("Trust check needs 1-3 'Watch for:' points")
    prose = [d["context"], d["task"], d["concept"]["lead"], d["concept"]["close"]] + [s["do"] for s in d["steps"] if s["do"]] + d["need"] + d["already"]
    if sum("**" in x for x in prose if x) < len([x for x in prose if x]) // 2:
        w.append("bold the 1-3 key words in most prose lines (context, task, concept, step Do lines)")
    for g in d["glossary"]:
        if not re.search(r"\[\[[^\]]*" + re.escape(g["label"].split(" (")[0]) + r"[^\]]*\]\]", md, re.I):
            w.append("glossary term never marked in the text: [[" + g["label"] + "]]")
    ch = d["concept"].get("check")
    if not ch:
        w.append("add one formative question: ## Check your understanding (Question:, 3-4 '- A: ...' options, Answer:, Why:)")
    elif not (ch["question"] and 3 <= len(ch["options"]) <= 4 and ch["answer"] and ch["why"]):
        e.append("Check your understanding needs Question:, 3-4 options '- A: text', Answer: and Why:")
    if len(d["practice"]) != 3:
        w.append("Practice should have exactly 3 items")
    if len(d["test"]["checks"]) > 3 or len(d["done"]) > 3:
        w.append("Test checks and Done when: max 3 each")
    return e, w


def classic(d, ui):
    """Map lesson data onto the page template's data schema. `ui` holds the page's interface texts in the learner's language."""
    def T(key, **kw):
        s = ui.get(key, key)
        for a, v in kw.items():
            s = s.replace("{%s}" % a, str(v))
        return s
    code = d["meta"]["kind"] in ("code", "workflow")
    parts = [{"id": re.sub(r"[^a-z0-9]+", "-", s["name"].lower().translate(UMLAUT)).strip("-"), "label": s["name"]} for s in d["steps"]]
    steps = []
    if d.get("compare"):
        steps.append({"kind": "compare", "heading": T("step_n", n=1, name=T("step_spot")), "bad": {"text": d["compare"]["bad"], "code": True},
                      "good": {"text": d["compare"]["good"], "code": True}, "question": d["compare"]["ask"], "next": T("next_step", name=d["steps"][0]["name"])})
    use = d["steps"][0]["use"] if d["steps"] else ""
    if d.get("scenario") and d["scenario"].get("situation"):
        steps.append({"kind": "choose", "heading": T("step_n", n=len(steps) + 1, name=T("step_choose")), "intro": use, "scenario": d["scenario"],
                      "question": d["scenario"].get("ask") or T("ask_choose"), "next": T("next_step", name=d["steps"][0]["name"])})
        use = ""
    for i, s in enumerate(d["steps"]):
        n = len(steps) + 1
        nxt = T("next_step", name=d["steps"][i + 1]["name"] if i + 1 < len(d["steps"]) else ui["sec_trust"])
        steps.append({"kind": "part", "part": parts[i]["id"], "heading": T("step_n", n=n, name=s["name"]), "intro": " ".join(x for x in ((use if i == 0 else s["use"]), s["why"]) if x), "example": s["example"] if s["example"]["good"] else None, "code": s["code"],
                      "instructions": s["instructions"], "question": s["ask"] if s["instructions"] else s["do"] + " " + s["ask"], "next": nxt})
    return {"title": d["title"], "meta_line": "  ·  ".join(x for x in [d["meta"]["track"], d["meta"]["topic"], T("meta_mission", n=d["meta"]["lesson"]) if d["meta"]["lesson"] else "", d["meta"]["time"]] if x),
            "your_mission": {"imagine": d["context"], "mission": d["task"] + " " + d["outcome"], "prereqs": d["need"] + d["already"], "next": T("next_start")},
            "concept": {"heading": d["concept"]["heading"], "before": d["concept"]["lead"], "body": d["concept"]["close"],
                        "toggles": d["concept"].get("toggles") or [],
                        "check": {k: v for k, v in (d["concept"].get("check") or {}).items() if k in ("question", "options", "answer", "why")} or None,
                        "visual": {"type": "cards", "items": d["concept"]["cards"]}, "image": d["concept"].get("image"), "next": T("next_build")},
            "artefact": {"name": d["meta"]["artefact"], "filename": d["meta"]["file"] or "artefact.md", "code": code, "parts": parts if d["meta"]["kind"] != "none" else [],
                         "template": {"name": d.get("template", {}).get("name", ""), "text": d.get("template", {}).get("text", ""), "how": ""}},
            "build": {"steps": steps},
            "test": {"heading": T("test_title", artefact=d["meta"]["artefact"][:1].lower() + d["meta"]["artefact"][1:]), "intro": d["test"]["do"], "instructions": d["test"]["instructions"], "privacy": d["test"]["privacy"],
                     "checks": d["test"]["checks"], "question": d["test"]["ask"], "next": T("next_other")},
            "trust": {"laws": d["trust"]["laws"], "watch": d["trust"]["watch"], "ask": d["trust"]["ask"], "next": T("next_test")},
            "other_ways": {"items": [{"tool": x["label"], "text": x["text"]} for x in d["other"]], "next": T("next_practice")},
            "practice": {"exercises": d["practice"], "next": T("next_wrap")},
            "closure": {},
            "glossary": [{"term": g["label"], "def": g["text"]} for g in d["glossary"]],
            "sources": d["sources"]}, ['"at": "1.1"'] + ['"part:%s": ""' % p["id"] for p in parts]


def ui_pack(lang="en"):
    """The page's built-in interface texts for one language, read from the template (key -> text)."""
    html = open(os.path.join(HERE, "..", "assets", "lesson-template.html"), encoding="utf-8").read()
    start = html.index("\n%s:{" % lang) + 1
    nxt = re.search(r"\n[a-z]{2}:\{", html[start:])
    block = html[start:start + nxt.start()] if nxt else html[start:]
    out = {}
    for k, v in re.findall(r'([A-Za-z_][A-Za-z0-9_]*):"((?:[^"\\]|\\.)*)"', block):
        try:
            out[k] = json.loads('"' + v + '"')
        except ValueError:
            out[k] = v
    return out


def main():
    global CONTENT, MISSIONS
    a = argparse.ArgumentParser()
    a.add_argument("lesson", nargs="?"); a.add_argument("out", nargs="?"); a.add_argument("--lang", default="en")
    a.add_argument("--learner", default="learner"); a.add_argument("--check", action="store_true")
    a.add_argument("--tool", default="claude-app", choices=TOOLS, help="the learner's AI tool: picks the [tool] variants of sections and steps")
    a.add_argument("--level", default="guided", choices=LEVELS, help="the learner's level in this topic: picks the [level] variants (e.g. a Go further step for fast-track)")
    a.add_argument("--example", help="JSON file with the working example adapted to the learner: situation, input, steps[], result, and why (Why this matters for the same situation)")
    a.add_argument("--content", help="folder holding missions/ and translations/ (default: this skill's folder)")
    a.add_argument("--ui", help="JSON file with translated interface texts for the page (keys as printed by --dump-ui)")
    a.add_argument("--dump-ui", action="store_true", help="print the English interface texts as JSON and exit")
    o = a.parse_args()
    if o.dump_ui:
        print(json.dumps(ui_pack("en"), ensure_ascii=False, indent=1)); return
    if not o.lesson:
        a.error("the mission file is required")
    if o.content:
        CONTENT = os.path.abspath(o.content); MISSIONS = os.path.join(CONTENT, "missions")
    t0 = time.time()
    tr_root = os.path.join(CONTENT, "translations") + os.sep
    lp = os.path.abspath(o.lesson)
    if lp.startswith(tr_root):
        # a translation file given as the mission: its folder names the language; it stands in for the English file when that is missing
        lang_tr, rest = os.path.relpath(lp, tr_root).split(os.sep, 1)
        en = os.path.join(MISSIONS, rest)
        if o.lang == "en":
            o.lang = lang_tr
        if not os.path.exists(en):
            os.makedirs(os.path.dirname(en), exist_ok=True)
            shutil.copyfile(lp, en)
            ty = os.path.join(os.path.dirname(lp), "_topic.yaml")
            if os.path.exists(ty) and not os.path.exists(os.path.join(os.path.dirname(en), "_topic.yaml")):
                shutil.copyfile(ty, os.path.join(os.path.dirname(en), "_topic.yaml"))
        o.lesson = en
    if not os.path.exists(o.lesson):
        print("ERROR: mission file not found: " + o.lesson); sys.exit(1)
    md, d = parse(o.lesson, o.lang, o.tool, o.level)
    mission_id = str(d["fm"].get("id", ""))
    err, warn = check(o.lesson, md, d)
    unknown = variant_tags(md) - set(TOOLS) - set(LEVELS)
    if unknown:
        err.append("unknown tag(s): " + ", ".join(sorted(unknown)) + " (use " + ", ".join(TOOLS + LEVELS) + ")")
    if o.check:
        for tl in sorted(variant_tags(md) & (set(TOOLS) | set(LEVELS)) - {o.tool, o.level}):
            e2, w2 = check(o.lesson, *parse(o.lesson, o.lang, tl if tl in TOOLS else o.tool, tl if tl in LEVELS else o.level))
            err += ["[%s] %s" % (tl, x) for x in e2 if x not in err]
            warn += ["[%s] %s" % (tl, x) for x in w2 if x not in warn]
    for x in warn:
        print("WARNING:", x)
    for x in err:
        print("ERROR:", x)
    if err:
        sys.exit(1)
    if o.check or not o.out:
        print("OK: lesson passes checks"); return
    summary = []
    if o.example:
        ex = json.load(open(o.example, encoding="utf-8"))
        sm = ex.pop("summary", None) or []
        if isinstance(sm, str):
            sm = [re.sub(r"^\s*[-*\u2022]\s+", "", l).strip() for l in sm.splitlines()]
        summary = [s for s in sm if isinstance(s, str) and s.strip()]
        if ex.get("why"):
            d["context"] = ex.pop("why")
        d["scenario"] = dict(d.get("scenario") or {}, **ex)
    uit = ui_pack("en")
    if o.lang[:2].lower() in ("es", "de"):
        uit.update(ui_pack(o.lang[:2].lower()))
    if o.ui:
        uit.update({k: v for k, v in json.load(open(o.ui, encoding="utf-8")).items() if isinstance(v, str)})
    data, lines = classic(d, uit)
    data["closure"] = {"summary": summary}
    data.update(lang=o.lang, learner=o.learner, mission_id=mission_id, build_id=format(int(time.time()), "x"))
    if o.ui:
        ui = json.load(open(o.ui, encoding="utf-8"))
        data["ui"] = {k: v for k, v in ui.items() if isinstance(v, str)}
    site_url = os.environ.get("AGENTUP_SITE_URL", "").strip()
    if site_url:
        data["site_url"] = site_url if site_url.endswith("/") else site_url + "/"
    html = open(os.path.join(HERE, "..", "assets", "lesson-template.html"), encoding="utf-8").read()
    html = html.replace("/*AGENTUP_DATA*/", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"), 1).replace("/*AGENTUP_STATE*/", "{\n" + ",\n".join(lines) + "\n}", 1)
    os.makedirs(os.path.dirname(os.path.abspath(o.out)), exist_ok=True)
    open(o.out, "w", encoding="utf-8").write(html)
    print("OK: wrote %s in %d ms" % (o.out, (time.time() - t0) * 1000))
    print("State lines for set_state.py: " + ", ".join(l.split(":")[0].strip('"') if not l.startswith('"part') else l.split('": ')[0].strip('"') for l in lines))


if __name__ == "__main__":
    main()
