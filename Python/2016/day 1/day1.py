with open('data.in', 'r') as f:
    L = f.readline()[:-1].split(', ')


def solve(L, p1):
    x, y = 0, 0
    d = 0 
    #0 1 2 3
    #N E S W
    visited = set() #previosuly visited cordinates
    for l in L:
        cmd = l[0]
        val = int(l[1:])
        if cmd == "R":
            d = (d+1)%4
        elif cmd == "L":
            d = (d-1)%4
        else:
            assert False
        for _ in range(val):
            if d == 0:
                y += 1
            elif d == 1:
                x += 1
            elif d == 2:
                y -= 1
            elif d == 3:
                x -= 1
            else:
                assert False
            if not p1:
                if (x, y) not in visited and not p1:
                    visited.add((x, y))
                else:
                    return abs(x)+ abs(y)
    return abs(x) + abs(y)


print(solve(L, True))
print(solve(L, False))
