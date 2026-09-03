with open("bundle.js", "r") as f:
    code = f.read()

idx_hj = code.find("function hj(")
idx_next = code.find("function ", idx_hj + 20)
hj_code = code[idx_hj:idx_next]

import re
for m in re.finditer(r'\.map\(', hj_code):
    start = max(0, m.start() - 30)
    end = min(len(hj_code), m.end() + 150)
    print("Map at", m.start(), ":", hj_code[start:end])

