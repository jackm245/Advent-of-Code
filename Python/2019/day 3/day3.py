with open('data.in', 'r') as F:
    W1 = [(i[0], i[1:].strip()) for i in F.readline().split(',')]
    W2 = [(i[0], i[1:].strip()) for i in F.readline().split(',')]

DX = {'R': 1, 'L': -1, 'U': 0, 'D':0}
DY = {'R': 0, 'L': 0, 'U': 1, 'D' : -1}

def conv_W_to_S(W):
    D = {}
    x, y, length = 0, 0, 0
    for w in W:
        for a in range(int(w[1])):
            x += DX[w[0]]
            y += DY[w[0]]
            length += 1
            if (x, y) not in D:
                D[(x, y)] = length
    return D

S1 = conv_W_to_S(W1)
S2 = conv_W_to_S(W2)
intersections = set(S1.keys())&set(S2.keys())
part1 = min([(abs(x)+abs(y)) for (x, y) in intersections])
part2 = min([S1[p]+S2[p] for p in intersections])
print(part1, part2)


