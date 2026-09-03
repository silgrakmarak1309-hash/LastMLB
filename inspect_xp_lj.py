with open("bundle.js", "r") as f:
    code = f.read()

idx_xp = code.find("function Xp(")
print("=== Xp function ===")
print(code[idx_xp:idx_xp+500])

idx_lj = code.find("function lj(")
print("\n=== lj function start ===")
print(code[idx_lj:idx_lj+500])

