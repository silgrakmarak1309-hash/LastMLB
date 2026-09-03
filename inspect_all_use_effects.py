with open("bundle.js", "r") as f:
    code = f.read()

import re
matches = list(re.finditer(r'm\.useEffect\(', code))
print(f"Total m.useEffect calls found: {len(matches)}")
for i, m in enumerate(matches):
    start = max(0, m.start() - 100)
    end = min(len(code), m.start() + 400)
    print(f"\n================ useEffect #{i+1} at index {m.start()} ================")
    print(code[start:end])

