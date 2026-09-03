with open("bundle.js", "r") as f:
    code = f.read()

target = "const hasLoadedListingsRef = m.useRef(false);  const prevFilterRef = m.useRef({ l: null, d: null });  const O = m.useCallback(async (isUserSearch = false) => {    if (!hasLoadedListingsRef.current || isUserSearch) {      k(true);    }    try {      const E = await Vp({ search: l || void 0, locationId: d || void 0, limit: 50 });      hasLoadedListingsRef.current = true;      v(prev => areDataEqual(prev, E) ? prev : E);    } catch {      if (toastRef.current && !hasLoadedListingsRef.current) {        toastRef.current.show(\"Failed to load listings\", \"error\");      }    } finally {      k(false);    }  }, [l, d]);  m.useEffect(() => {    const isFilterChange = (prevFilterRef.current.l !== l || prevFilterRef.current.d !== d);    if (prevFilterRef.current.l === null) {      // First initial mount      prevFilterRef.current = { l, d };      O(false);    } else if (isFilterChange) {      prevFilterRef.current = { l, d };      O(true);    }  }, [O, l, d]);  const userId = e?.id;  m.useEffect(() => {    if (userId) {      syncLocalListingsToSupabase().then(() => O(false)).catch(() => {});      Yp(userId).then(favs => {        I(prev => {          const arr = Array.from(prev);          return areDataEqual(arr, favs) ? prev : new Set(favs);        });      }).catch(() => {});    }  }, [userId, O]);"

replacement = "const hasLoadedListingsRef = m.useRef(false);  const prevFilterRef = m.useRef({ l: null, d: null });  const O = m.useCallback(async (isUserSearch = false) => {    if (!hasLoadedListingsRef.current) {      k(true);    }    try {      const E = await Vp({ search: l || void 0, locationId: d || void 0, limit: 50 });      hasLoadedListingsRef.current = true;      v(prev => areDataEqual(prev, E) ? prev : E);    } catch {      if (toastRef.current && !hasLoadedListingsRef.current) {        toastRef.current.show(\"Failed to load listings\", \"error\");      }    } finally {      k(false);    }  }, [l, d]);  m.useEffect(() => {    const isFilterChange = (prevFilterRef.current.l !== l || prevFilterRef.current.d !== d);    if (prevFilterRef.current.l === null) {      prevFilterRef.current = { l, d };      O(false);    } else if (isFilterChange) {      prevFilterRef.current = { l, d };      O(true);    }  }, [O, l, d]);  const userId = e?.id;  m.useEffect(() => {    if (userId) {      Yp(userId).then(favs => {        I(prev => {          const arr = Array.from(prev);          return areDataEqual(arr, favs) ? prev : new Set(favs);        });      }).catch(() => {});    }  }, [userId]);"

if target in code:
    code = code.replace(target, replacement)
    print("Exact target found and replaced!")
else:
    print("Target not found exactly, checking substring...")
    pos = code.find("const hasLoadedListingsRef = m.useRef(false);")
    print("Found pos:", pos)
    end_pos = code.find("m.useEffect(() => {    if (g.length > 1)", pos)
    print("Found end_pos:", end_pos)
    old_block = code[pos:end_pos]
    code = code[:pos] + replacement + "  " + code[end_pos:]
    print("Replaced block successfully!")

with open("bundle.js", "w") as f:
    f.write(code)

