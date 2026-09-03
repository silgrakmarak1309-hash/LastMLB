with open("bundle.js", "r") as f:
    code = f.read()

idx = code.find("Top PRO Listings")
print(code[idx-200:idx+2500])

