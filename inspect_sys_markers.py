with open("bundle.js", "r") as f:
    code = f.read()

import re

for m in re.finditer(r'\[SYS_[A-Z_]+\]', code):
    start = max(0, m.start() - 60)
    end = min(len(code), m.end() + 100)
    print("Match at", m.start(), ":", code[start:end])

