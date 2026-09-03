with open("bundle.js", "r") as f:
    code = f.read()

idx = code.find("Failed to load your ads")
print(code[idx-600:idx+600])

