with open("bundle.js", "r") as f:
    code = f.read()

idx = code.find("function bw({")
print(code[idx+3200:idx+4500])

