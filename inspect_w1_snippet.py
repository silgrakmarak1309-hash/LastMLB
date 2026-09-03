with open("bundle.js", "r") as f:
    code = f.read()

idx = code.find("hasLoadedListingsRef")
print(code[idx-50:idx+1500])

