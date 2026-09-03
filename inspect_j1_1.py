with open("bundle.js", "r") as f:
    code = f.read()

idx_j1 = code.find("async function j1(")
idx_1 = code.find("async function _1(")
idx_xd = code.find("async function xd(", idx_1)

print("=== j1 length ===", idx_1 - idx_j1)
print(code[idx_j1:idx_j1+500])
print("...")
print(code[idx_1-200:idx_1])

print("\n=== _1 length ===", idx_xd - idx_1)
print(code[idx_1:idx_1+500])
print("...")
print(code[idx_xd-200:idx_xd])

