with open("bundle.js", "r") as f:
    code = f.read()

import re

for m in re.finditer(r'a\.jsx\(Oc,\s*\{[^}]*\}\)', code):
    pos = m.start()
    print(f"=== Oc at {pos} ===")
    print(code[max(0, pos-120):min(len(code), pos+150)])

for m in re.finditer(r'a\.jsx\(Oc,\{\}\)', code):
    pos = m.start()
    print(f"=== Oc at {pos} ===")
    print(code[max(0, pos-120):min(len(code), pos+150)])

