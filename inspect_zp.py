with open("bundle.js", "r") as f:
    code = f.read()

idx = code.find("zp.Provider")
if idx == -1:
    idx = code.find("zp=")
print(code[idx-500:idx+1500])

