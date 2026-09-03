with open("bundle.js", "r") as f:
    code = f.read()

import re
for m in re.finditer(r'(async )?function (v1|L1|O1|A1|x1)\(', code):
    print(m.group(0), "at", m.start())

