with open("bundle.js", "r") as f:
    code = f.read()

import re

# Let's inspect views:
# 1. ListingDetail view
# 2. PostListing / CreateListing view
# 3. User Ads / MyAds view
# 4. User Favorites view
# 5. User Account / Profile view
# 6. User Recharge / Plans view
# 7. Admin Views (Overview, Users, Listings, Normal Posts, Top PRO, Monthly Plans, Transactions, Banners, Categories, Locations, Plans, Settings)

views = [
    ("ListingDetail", "function F1(", "function j("),
    ("CreateListing", "function C1(", "function Xp("),
    ("MyAds", "function qp(", "function Yp("),
    ("Favorites", "function Yp(", "function Wp("),
    ("Account", "function Z1(", "function W1("),
    ("UserRecharge", "function lj(", "function pj("),
]

for name, start_p, end_p in views:
    idx_s = code.find(start_p)
    if idx_s != -1:
        print(f"Found {name} at {idx_s}")
    else:
        print(f"NOT FOUND: {name} with pattern {start_p}")

