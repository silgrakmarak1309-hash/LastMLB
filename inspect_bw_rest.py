with open("bundle.js", "r") as f:
    code = f.read()

idx = code.find("function bw({")
print(code[idx+1800:idx+4500])

