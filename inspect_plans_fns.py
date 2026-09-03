with open("bundle.js", "r") as f:
    code = f.read()

idx_v1 = code.find("async function v1()")
print("=== v1() ===")
print(code[idx_v1:idx_v1+1500])

idx_xp = code.find("function Xp(")
if idx_xp == -1:
    idx_xp = code.find("async function Xp(")
print("\n=== Xp() ===")
print(code[idx_xp:idx_xp+1500])

