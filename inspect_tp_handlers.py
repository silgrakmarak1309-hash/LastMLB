with open("bundle.js", "r") as f:
    code = f.read()

idx_tp = code.find("function TopProRequestsView(")
idx_pj = code.find("function pj(", idx_tp)
tp_code = code[idx_tp:idx_pj]

import re
for m in re.finditer(r'const handle[A-Za-z0-9_]+', tp_code):
    print(m.group(0), "at", m.start())

