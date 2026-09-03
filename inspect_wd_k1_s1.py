with open("bundle.js", "r") as f:
    code = f.read()

idx_wd = code.find("async function wd(")
idx_k1 = code.find("async function k1(")
idx_s1 = code.find("async function S1(")
idx_n1 = code.find("async function N1(", idx_s1)

print("=== wd length ===", idx_k1 - idx_wd)
print(code[idx_wd:idx_wd+300])

print("\n=== k1 length ===", idx_s1 - idx_k1)
print(code[idx_k1:idx_k1+300])

print("\n=== s1 length ===", idx_n1 - idx_s1)
print(code[idx_s1:idx_s1+300])

