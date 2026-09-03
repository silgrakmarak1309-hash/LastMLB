with open("bundle.js", "r") as f:
    code = f.read()

idx = 602180
print("=== Around 602180 ===")
fn_start = code.rfind("function ", 0, idx)
print(code[fn_start:idx+500])

