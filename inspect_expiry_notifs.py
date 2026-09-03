with open("bundle.js", "r") as f:
    code = f.read()

idx = code.find("function checkProExpiryNotifications(")
if idx == -1:
    idx = code.find("checkProExpiryNotifications")
print(code[idx-100:idx+1200])

