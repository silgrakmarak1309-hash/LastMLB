with open("bundle.js", "r") as f:
    code = f.read()

idx_tp = code.find("function TopProRequestsView(")
idx_np = code.find("function NormalPostRequestsView(", idx_tp)
if idx_np == -1:
    idx_np = code.find("function pj(", idx_tp)
print(f"TopProRequestsView starts at {idx_tp}, next function at {idx_np}, length {idx_np - idx_tp}")

