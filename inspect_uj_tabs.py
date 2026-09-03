with open("bundle.js", "r") as f:
    code = f.read()

idx_uj = code.find("function uj(")
idx_tabs = code.find("r === \"", idx_uj)
print(code[idx_tabs:idx_tabs+2500])

