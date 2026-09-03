with open("bundle.js", "r") as f:
    code = f.read()

import re

for m in re.finditer(r'\.Provider', code):
    pos = m.start()
    fn_start = code.rfind("function ", 0, pos)
    print(f"Provider in {code[fn_start:fn_start+60]}:")
    print(code[pos-20:pos+150])
    print("\n")

