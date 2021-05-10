def get_data():
    with open('data.in', 'r') as f:
        data = [i.strip() for i in f]
    active = set()
    for row, line in enumerate(data):
        for column, char in enumerate(line):
            if char == '#':
                active.add((row, column, 0, 0))
    return active
def solve(p1):
    active = get_data()
    for _ in range(6):
        new_active = set()
        w_range = (range(-8, 8) if not p1 else [0])
        for x in range(-15, 15):
            for y in range(-15, 15):
                for z in range(-8, 8):
                    for w in w_range:
                        nbr = 0
                        for dx in [-1, 0, 1]:
                            for dy in [-1, 0, 1]:
                                for dz in [-1, 0, 1]:
                                    for dw in [-1, 0, 1]:
                                        if not(dx == 0 and dy == 0 and dz == 0 and dw == 0):
                                            if (x+dx, y+dy, z+dz, w+dw) in active:
                                                nbr += 1
                        if (x, y, z, w) not in active and nbr == 3:
                            new_active.add((x, y, z, w))
                        if (x, y, z, w) in active and (nbr == 2 or nbr == 3):
                            new_active.add((x, y, z, w))
        active = new_active
    return len(active)

print(solve(True))
print(solve(False))
