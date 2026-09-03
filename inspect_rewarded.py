with open("bundle.js", "r") as f:
    code = f.read()

idx = code.find("function RewardedProAdSection(")
print(code[idx:idx+2500])

