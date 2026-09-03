with open("bundle.js", "r") as f:
    code = f.read()

positions = [1092901, 1122309, 1136623, 1138893, 1204631]
for pos in positions:
    fn_start = code.rfind("function ", 0, pos)
    print(f"=== Function around {pos} ({code[fn_start:fn_start+40]}) ===")
    print(code[fn_start:fn_start+300])

