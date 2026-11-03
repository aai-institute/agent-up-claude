#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Update one live-state value in a built lesson page (no rebuild).

Usage:  python3 set_state.py <page.html> <key> <value>
Keys:   part:<step> (last step = final asset: copy button, download)   at (e.g. "3.2")
Only the matching line inside <script id="agentup-state"> changes.
"""
import json, re, sys

if len(sys.argv) != 4:
    print(__doc__)
    sys.exit(2)
path, key, value = sys.argv[1:4]
html = open(path, encoding="utf-8").read()
m = re.search(r'(<script id="agentup-state" type="application/json">)(.*?)(</script>)', html, re.S)
if not m:
    sys.exit("state block not found")
block = m.group(2)
line = re.compile(r'^"' + re.escape(key) + r'": .*?(,?)$', re.M)
if not line.search(block):
    sys.exit("key not found: " + key)
new_val = json.dumps(value, ensure_ascii=False).replace("</", "<\\/")
block = line.sub(lambda mm: '"%s": %s%s' % (key, new_val, mm.group(1)), block, count=1)
json.loads(block)  # must stay valid JSON
html = html[:m.start(2)] + block + html[m.end(2):]
open(path, "w", encoding="utf-8").write(html)
print("OK:", key, "updated")
