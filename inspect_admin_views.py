with open("bundle.js", "r") as f:
    code = f.read()

# Inspect Admin Layout (qj)
idx_qj = code.find("function qj(")
print("=== Admin Layout (qj) ===")
print(code[idx_qj:idx_qj+2000])

