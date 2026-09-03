with open("bundle.js", "r") as f:
    code = f.read()

idx = code.find("syncLocalListingsToSupabase().then")
print(code[idx-1200:idx+800])

