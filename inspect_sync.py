with open("bundle.js", "r") as f:
    code = f.read()

idx = code.find("function syncLocalListingsToSupabase")
if idx == -1:
    idx = code.find("syncLocalListingsToSupabase")
print(code[idx:idx+2500])

