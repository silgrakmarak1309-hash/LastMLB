with open("bundle.js", "r") as f:
    code = f.read()

idx = code.find("async function checkProExpiryNotifications(")
print(code[idx:idx+2500])

