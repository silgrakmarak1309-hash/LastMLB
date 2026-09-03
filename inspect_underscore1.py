with open("bundle.js", "r") as f:
    code = f.read()

idx_1 = code.find("async function _1(")
print("=== _1() ===")
print(code[idx_1:idx_1+2000])

