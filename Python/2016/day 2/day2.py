from copy import deepcopy
with open('data.in', 'r') as f:
    L = [l[:-1] for l in f]

def part_1():
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    r, c = 1, 1 # starting pos on 5
    pword = []
    for l in L:
        for i in [j for j in l]:
            #print(i)
            #instruction
            if i == "U":
                r = (r-1)
            elif i == "D":
                r = (r+1)
            elif i == "L":
                c = (c-1)
            elif i == "R":
                c = (c+1)
            else:
                assert False
            if c > 2:
                c = 2
            elif c < 0:
                c = 0
            if r > 2:
                r = 2
            elif r < 0:
                r = 0
            #print(r, c)
        pword.append(str(keypad[r][c]))
    return ''.join(pword)

def part_2():
    pword = []
    keypad = [ \
        ['_', '_', '1', '_', '_'], \
        ['_', '2', '3', '4', '_'], \
        ['5', '6', '7', '8', '9'], \
        ['_', 'A', 'B', 'C', '_'], \
        ['_', '_', 'D', '_', '_']]
    r, c = 2, 0 # starting pos on 5
    #nr, nc = 2, 0
    for l in L:
        nr = deepcopy(r)
        nc = deepcopy(c)
        #print("="*80)
        #print('-' + keypad[r][c])
        for i in [j for j in l]:
            #print(i)
            #instruction
            if i == "U":
                nr = r-1
            elif i == "D":
                nr = r+1
            elif i == "L":
                nc = c-1
            elif i == "R":
                nc = c+1
            else:
                assert False
            if nr > 4:
                nr = 4
            elif nr < 0:
                nr = 0

            if nc > 4:
                nc = 4
            elif nc < 0:
                nc = 0
            if keypad[nr][nc] != '_':
                r, c = deepcopy(nr), deepcopy(nc)     
            else:
                nr, nc = deepcopy(r), deepcopy(c)
            #print(r, c)
            #print('=', keypad[r][c], r, c, nr, nc)
        pword.append(keypad[r][c])
    return ''.join(pword)

print(part_1())
print(part_2())


