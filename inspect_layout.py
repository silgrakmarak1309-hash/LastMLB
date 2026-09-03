with open("bundle.js", "r") as f:
    code = f.read()

idx = code.find("function jj()")
if idx == -1:
    idx = code.find("function jj(")
print("=== App / Routes jj ===")
print(code[idx:idx+2500])

