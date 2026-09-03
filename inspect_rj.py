with open("bundle.js", "r") as f:
    code = f.read()

idx = code.find("function rj()")
if idx == -1:
    idx = code.find("function rj(")
print("=== Favorites rj ===")
print(code[idx:idx+1500])

