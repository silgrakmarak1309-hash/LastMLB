with open("bundle.js", "r") as f:
    code = f.read()

import re

for i, m in enumerate(re.finditer(r'setInterval\(', code)):
    pos = m.start()
    fn_start = code.rfind("function ", 0, pos)
    print(f"=== Interval #{i+1} in function {code[fn_start:fn_start+50]} ===")
    print(code[pos-50:pos+300])
    print("\n")

