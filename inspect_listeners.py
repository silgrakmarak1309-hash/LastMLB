with open("bundle.js", "r") as f:
    code = f.read()

import re

for m in re.finditer(r'addEventListener\(', code):
    pos = m.start()
    print(code[pos-40:pos+150])

