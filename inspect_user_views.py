with open("bundle.js", "r") as f:
    code = f.read()

# Inspect UserRecharge (lj)
idx_lj = code.find("function lj(")
print("=== UserRecharge (lj) ===")
print(code[idx_lj:idx_lj+1800])

# Inspect Account (Z1)
idx_z1 = code.find("function Z1(")
print("\n=== Account (Z1) ===")
print(code[idx_z1:idx_z1+1500])

