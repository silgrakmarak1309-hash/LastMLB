with open("bundle.js", "r") as f:
    code = f.read()

idx_uj = code.find("function uj(")
print(code[idx_uj:idx_uj+2500])

