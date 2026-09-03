with open("bundle.js", "r") as f:
    code = f.read()

import re

# 1. Let's check how getAllPlans / v1 are used
print("=== v1 usages ===")
for m in re.finditer(r'\bv1\(', code):
    print("v1 call at:", m.start(), code[max(0, m.start()-30):min(len(code), m.start()+50)])

# 2. Let's check how recharge requests are created in user recharge page lj
idx_lj = code.find("function lj(")
print("\n=== lj (User Recharge Page) ===")
print("lj position:", idx_lj)

