with open("bundle.js", "r") as f:
    code = f.read()

idx_pj = code.find("function pj(")
idx_vj = code.find("function vj(", idx_pj)
pj_code = code[idx_pj:idx_vj]

# Let's find handleApprove, handleReject, setRejectTargetId, etc.
import re
print("=== Handlers in pj ===")
for m in re.finditer(r'const handle[A-Za-z0-9_]+', pj_code):
    print(m.group(0))

