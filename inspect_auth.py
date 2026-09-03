with open("bundle.js", "r") as f:
    code = f.read()

idx = code.find("function bw({")
if idx == -1:
    idx = code.find("function bw(")
print(code[idx:idx+2500])

