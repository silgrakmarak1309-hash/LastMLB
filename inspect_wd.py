with open("bundle.js", "r") as f:
    code = f.read()

idx_wd = code.find("async function wd(")
print(code[idx_wd:idx_wd+2500])

