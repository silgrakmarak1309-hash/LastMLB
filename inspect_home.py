with open("bundle.js", "r") as f:
    code = f.read()

idx = code.find("syncLocalListingsToSupabase")
print(code[idx-500:idx+1500])

