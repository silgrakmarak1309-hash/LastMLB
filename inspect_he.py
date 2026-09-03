with open("bundle.js", "r") as f:
    code = f.read()

idx = code.find("function he(")
if idx == -1:
    idx = code.find("useToast")
print(code[idx-200:idx+800])

