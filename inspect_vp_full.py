with open("bundle.js", "r") as f:
    code = f.read()

idx = code.find("async function Vp(")
idx_end = code.find("async function o1(", idx)
print(code[idx:idx_end])

