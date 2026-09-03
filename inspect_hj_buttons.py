with open("bundle.js", "r") as f:
    code = f.read()

idx_hj = code.find("function hj(")
idx_xj = code.find("function xj(", idx_hj)
hj_code = code[idx_hj:idx_xj]

import re
idx_render = hj_code.find("filteredUsers.map")
print("=== User card in hj ===")
print(hj_code[idx_render:idx_render+3000])

