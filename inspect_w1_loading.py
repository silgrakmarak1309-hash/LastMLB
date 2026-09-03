with open("bundle.js", "r") as f:
    code = f.read()

idx_w1 = code.find("function W1(){")
idx_end = code.find("function Z1(", idx_w1)
if idx_end == -1:
    idx_end = code.find("function lj(", idx_w1)

w1_code = code[idx_w1:idx_end]
print("W1 code:")
print(w1_code)

