with open("bundle.js", "r") as f:
    code = f.read()

idx_pj = code.find("function pj(")
idx_vj = code.find("function vj(", idx_pj)
pj_code = code[idx_pj:idx_vj]

import re
for m in re.finditer(r'\.map\(', pj_code):
    start = max(0, m.start() - 30)
    end = min(len(pj_code), m.end() + 150)
    print("Map at", m.start(), ":", pj_code[start:end])

