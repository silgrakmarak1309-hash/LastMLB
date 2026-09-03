with open("bundle.js", "r") as f:
    code = f.read()

idx = code.find("function Wp(")
if idx == -1:
    idx = code.find("function Wp({")
print(code[idx:idx+2500])

