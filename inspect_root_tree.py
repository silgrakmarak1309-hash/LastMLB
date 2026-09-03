with open("bundle.js", "r") as f:
    code = f.read()

idx = code.find("function _j(){")
if idx == -1:
    idx = code.find("mountApp")
print(code[idx-500:idx+1500])

