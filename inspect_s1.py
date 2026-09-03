with open("bundle.js", "r") as f:
    code = f.read()

idx = code.find("function s1(){")
print(code[idx:idx+1500])

