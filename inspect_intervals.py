with open("bundle.js", "r") as f:
    code = f.read()

import re
matches = list(re.finditer(r'setInterval\(', code))
print(f"Total setInterval calls found: {len(matches)}")
for i, m in enumerate(matches):
    start = max(0, m.start() - 250)
    end = min(len(code), m.start() + 450)
    print(f"\n================ INTERVAL #{i+1} at index {m.start()} ================")
    print(code[start:end])

