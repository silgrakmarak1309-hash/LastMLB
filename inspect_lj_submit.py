with open("bundle.js", "r") as f:
    code = f.read()

idx_lj = code.find("function lj(")
idx_submit = code.find("handleSubmit", idx_lj)
if idx_submit != -1:
    print("=== handleSubmit in lj ===")
    print(code[idx_submit:idx_submit+2500])
else:
    print("handleSubmit not found in lj")

