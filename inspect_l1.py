with open("bundle.js", "r") as f:
    code = f.read()

idx = code.find("function l1(){")
if idx == -1:
    idx = code.find("function l1(")
print(code[idx:idx+800])

