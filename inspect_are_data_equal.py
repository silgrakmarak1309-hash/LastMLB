with open("bundle.js", "r") as f:
    code = f.read()

idx = code.find("function areDataEqual")
if idx == -1:
    idx = code.find("areDataEqual")
print(code[idx:idx+1500])

