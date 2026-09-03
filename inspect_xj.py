with open("bundle.js", "r") as f:
    code = f.read()

idx_xj = code.find("function xj(")
idx_wj = code.find("function wj(", idx_xj)
print("=== xj (Admin PRO Plans Component) ===")
print(code[idx_xj:idx_wj])

