with open("bundle.js", "r") as f:
    code = f.read()

idx = code.find("function W1(){")
idx_end = code.find("function Z1(", idx)
if idx_end == -1:
    idx_end = code.find("function lj(", idx)
w1_code = code[idx:idx_end]

idx_recent = w1_code.find("Recent Listings")
print("Around Recent Listings:")
print(w1_code[idx_recent-500:idx_recent+1500])

idx_toppro = w1_code.find("Top PRO Listings")
print("\nAround Top PRO Listings:")
print(w1_code[idx_toppro-500:idx_toppro+1500])

