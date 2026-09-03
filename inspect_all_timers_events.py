with open("bundle.js", "r") as f:
    code = f.read()

import re

print("All addEventListener in bundle.js:")
for m in re.finditer(r'addEventListener\([\'"](\w+)[\'"]', code):
    print(m.group(0))

print("\nAll CustomEvent in bundle.js:")
for m in re.finditer(r'new CustomEvent\([\'"](\w+)[\'"]', code):
    print(m.group(0))

print("\nAll dispatchEvent in bundle.js:")
for m in re.finditer(r'dispatchEvent\(', code):
    pos = m.start()
    print(code[pos-20:pos+150])

