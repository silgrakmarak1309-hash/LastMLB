with open("bundle.js", "r") as f:
    code = f.read()

idx = code.find("function ta({")
if idx == -1:
    idx = code.find("function ta(")
print("=== Listing Card ta ===")
print(code[idx:idx+2500])

