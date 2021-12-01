from pprint import pprint as p


with open('test.in', 'r') as f:
    T = {} # name: towers
    for l in f:
        l = l.strip()
        name = l[:4]
        if len (l) > 14: #if it has other towers
            tl = l.split('->')
            tll = tl[1].split(', ')
            print(tll)
        else:
            tll = None
        T[name] = tll
    p(T)
    for t, tl in T.copy().items():
        if tl is not None:
            for i in tl:
                try:
                    T[i]
                except KeyError:
                    T[i] = None
    p(T)
    for t, tl in T.items():
        if tl is not None:
            for i in tl:
                if T[i] is not None:
                    tl[tl.index(i)] = T[i]
    p(T)
