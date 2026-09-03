with open("bundle.js", "r") as f:
    code = f.read()

idx = code.find("function jj(){")
print("=== jj definition ===")
print(code[idx:idx+1200])

idx_ky = code.find("var ky=")
if idx_ky == -1:
    idx_ky = code.find("const ky=")
print("=== ky definition ===")
print(code[idx_ky:idx_ky+400])

