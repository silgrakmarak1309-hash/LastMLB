with open("bundle.js", "r") as f:
    code = f.read()

import re

# 1. Inspect user management (active/inactive, block/unblock)
print("=== User Management in Admin (Search user status update) ===")
matches = [m.start() for m in re.finditer(r'profiles.*update|update.*profiles|is_blocked|account_status', code)]
print(f"Found {len(matches)} occurrences")

# Find User Management component in Admin
idx_uj = code.find("function uj(")
idx_uj_end = code.find("function Pt(", idx_uj)
print("Admin component length:", idx_uj_end - idx_uj)

# Let's search inside uj for users tab / subcomponents
idx_users_view = code.find("function UsersView", idx_uj) if "function UsersView" in code else code.find("Users Management", idx_uj)
print("Users Management in uj at:", idx_users_view)

