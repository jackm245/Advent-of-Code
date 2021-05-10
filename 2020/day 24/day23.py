with open('data.in', 'r') as f:
    L = [l.strip() for l in f]

#part 1
BLACK = set()
for l in L:
    #3 coordinate grid system
    # https://www.redblobgames.com/grids/hexagons/
    x, y, z = 0, 0, 0
    while len(l) > 0:
        if l.startswith('e'):
            x += 1
            y -= 1
            l = l[1:]
        elif l.startswith('se'):
            y -= 1
            z += 1
            l = l[2:]
        elif l.startswith('sw'):
            x -= 1
            z += 1
            l = l[2:]
        elif l.startswith('w'):
            x -= 1
            y += 1
            l = l[1:]
        elif l.startswith('nw'):
            y += 1
            z -= 1
            l = l[2:]
        elif l.startswith('ne'):
            x += 1
            z -= 1
            l = l[2:]
        else:
            assert Faslse
    if (x, y, z) in BLACK:
        BLACK.remove((x, y, z))
    else:
        BLACK.add((x, y, z))
print(len(BLACK)) #part 1 ans

#part 2
for _ in range(100):
    NEW_B = set()
    TO_CHECK = set()
    for (x, y, z) in BLACK:
        TO_CHECK.add((x, y, z))
        for (dx, dy, dz) in [(1, -1, 0), (0, -1, 1), (-1, 0, 1), (-1, 1, 0), (0, 1, -1), (1, 0, -1)]:
            TO_CHECK.add((x+dx, y+dy, z+dz))

    for (x, y, z) in TO_CHECK:
        nbrs = 0
        #x y z
        for (dx, dy, dz) in [(1, -1, 0), (0, -1, 1), (-1, 0, 1), (-1, 1, 0), (0, 1, -1), (1, 0, -1)]:
            if (x+dx, y+dy, z+dz) in BLACK:
                nbrs += 1
        #if (x, y,z) in B and
        if (x, y, z) in BLACK and not(nbrs == 0 or nbrs > 2):
            NEW_B.add((x, y, z))
        elif (x, y, z) not in BLACK and nbrs == 2:
            NEW_B.add((x, y, z))
    BLACK = NEW_B
print(len(BLACK)) #part 2 ans
            

