with open("bundle.js", "r") as f:
    code = f.read()

idx = code.find("var St=")
if idx == -1:
    idx = code.find("const St=")
if idx == -1:
    idx = code.find("St=")
print("=== Finding St ===")
print(code[idx:idx+800])

