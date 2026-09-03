with open("bundle.js", "r") as f:
    code = f.read()

idx_1 = code.find("async function _1(")
print("=== _1() part 2 ===")
print(code[idx_1+1000:idx_1+3000])

