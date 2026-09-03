with open("bundle.js", "r") as f:
    code = f.read()

idx_v1 = code.find("function V1()")
if idx_v1 == -1:
    idx_v1 = code.find("function V1(")
print("=== Search V1 ===")
print(code[idx_v1:idx_v1+1500])

