with open("bundle.js", "r") as f:
    code = f.read()

idx = code.find("function bw({")
print(code[idx+4200:idx+5500])

