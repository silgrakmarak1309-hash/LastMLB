with open("bundle.js", "r") as f:
    code = f.read()

idx = code.find("async function syncCloudConfig(")
if idx != -1:
    print(code[idx:idx+2500])
else:
    print("syncCloudConfig not found, let's search for syncCloud")
    for m in re.finditer(r'syncCloud', code):
        print(code[m.start()-50:m.start()+200])

