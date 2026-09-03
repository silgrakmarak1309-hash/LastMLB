with open("bundle.js", "r") as f:
    code = f.read()

idx_hj = code.find("function hj(")
idx_fj = code.find("function fj(", idx_hj)
print("=== hj (Users Management) ===")
print(code[idx_hj:idx_fj])

