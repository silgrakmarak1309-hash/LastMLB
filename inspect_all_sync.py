with open("bundle.js", "r") as f:
    code = f.read()

# Print Jp completely
idx_jp = code.find("async function Jp()")
idx_j1 = code.find("async function j1(", idx_jp)
print("=== Jp() ===")
print(code[idx_jp:idx_j1])

# Print j1 and _1 completely
idx_w1 = code.find("async function w1(", idx_j1)
print("\n=== j1() & _1() ===")
print(code[idx_j1:idx_w1])

# Print k1 & S1 & wd completely
idx_wd = code.find("async function wd(")
idx_x1 = code.find("async function x1()", idx_wd)
print("\n=== wd(), k1(), S1() ===")
print(code[idx_wd:idx_x1])

