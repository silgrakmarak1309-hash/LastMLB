with open("bundle.js", "r") as f:
    code = f.read()

def show_fn(name, max_len=3000):
    idx = code.find(f"function {name}(")
    if idx == -1:
        idx = code.find(f"async function {name}(")
    if idx == -1:
        print(f"=== {name} NOT FOUND ===")
        return
    print(f"\n==================== {name} ====================")
    print(code[idx:idx+max_len])

# 1. Users management
show_fn("xj", 3500)

# 2. Plans management
show_fn("vj", 3500)

# 3. Settings management
show_fn("wj", 3500)

