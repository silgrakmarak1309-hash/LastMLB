with open("bundle.js", "r") as f:
    code = f.read()

import re

print("All setInterval in bundle.js:")
for m in re.finditer(r'setInterval\((.*?)\)', code):
    print(m.group(0)[:150])
    print("-" * 30)

