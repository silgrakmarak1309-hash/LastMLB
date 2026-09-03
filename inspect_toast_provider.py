with open("bundle.js", "r") as f:
    code = f.read()

idx = code.find("zp.Provider")
idx_fn = code.rfind("function ", 0, idx)
print(code[idx_fn:idx+300])

