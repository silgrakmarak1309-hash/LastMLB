with open("bundle.js", "r") as f:
    code = f.read()

idx = code.find("function W1(){")
idx_end = code.find("function Z1(", idx)
if idx_end == -1:
    idx_end = code.find("function lj(", idx)
w1_code = code[idx:idx_end]

print("Full component code for W1:")
print(w1_code[:3000])

