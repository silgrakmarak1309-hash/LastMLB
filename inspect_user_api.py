with open("bundle.js", "r") as f:
    code = f.read()

import re

def print_section(query, length=2500):
    idx = code.find(query)
    if idx != -1:
        print(f"\n=== Found '{query}' at {idx} ===")
        print(code[idx:idx+length])
    else:
        print(f"NOT FOUND: '{query}'")

print_section("async function Ic()")
print_section("async function wd(")
print_section("async function k1(")
print_section("async function S1(")
print_section("function Ct(")

