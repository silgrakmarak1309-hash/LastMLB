with open("bundle.js", "r") as f:
    code = f.read()

import re
matches = list(re.finditer(r'(async )?function [A-Za-z0-9_$]+\(', code[894000:915000]))
for m in matches:
    print(m.group(0), "at relative", m.start(), "abs", 894000 + m.start())

