with open("bundle.js", "r") as f:
    code = f.read()

idx_ic = code.find("async function Ic()")
print(code[idx_ic:idx_ic+3500])

