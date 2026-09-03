with open("bundle.js", "r") as f:
    code = f.read()

idx = code.find("function bw({children:e}){")
idx_end = code.find("function Ae(){", idx)
print(code[idx:idx_end])

