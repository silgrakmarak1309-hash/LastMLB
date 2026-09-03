with open("bundle.js", "r") as f:
    code = f.read()

idx_bw = code.find("function bw({children:e})")
idx_ae = code.find("function Ae()", idx_bw)
print("=== AuthProvider bw ===")
print(code[idx_bw:idx_ae])

