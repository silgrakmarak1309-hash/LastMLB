with open("bundle.js", "r") as f:
    code = f.read()

idx_pj = code.find("function pj(")
idx_vj = code.find("function vj(", idx_pj)
print(f"pj index: {idx_pj}, vj index: {idx_vj}, length: {idx_vj - idx_pj}")

