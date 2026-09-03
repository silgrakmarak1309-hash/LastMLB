with open("bundle.js", "r") as f:
    code = f.read()

idx = code.find("function RewardedProAdSection")
if idx == -1:
    idx = code.find("RewardedProAdSection")
print(code[idx:idx+3500])

