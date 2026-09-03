with open("bundle.js", "r") as f:
    code = f.read()

idx_l1 = code.find("async function L1(")
idx_o1 = code.find("async function O1(")
idx_v1 = code.find("async function v1(")

print("=== L1 ===")
print(code[idx_l1:idx_l1+1200])

print("\n=== O1 ===")
print(code[idx_o1:idx_o1+1200])

