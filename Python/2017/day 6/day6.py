import re

with open('data.in', 'r') as f:
    b = list(map(int, re.findall(r'\d+', f.readline())))
#print(b)


def solve(p1):
    B = set()
    B.add(', '.join(list(map(str, b))))
    cycles = 1
    while True:
        #print(B)
        #print(b)
        #get bank with highest value (if tied go lowest val):
        highest = b.index(max(b))
        d = b[highest]
        b[highest] = 0
        #print(b)
        #now redsitribut them
        #use mod / div to work out how much each person gets, and what final person gets
        m = d // (len(b)-1)
        l = d - m*(len(b)-1)
        if m == 0:
            l = 0
            m=1
            n = d
        else:
            n = len(b)-1
        for i in range(n):
            b[(highest+i+1)%len(b)] += m
        b[(highest+i+2)%len(b)] += l
        #print(d, m, l)
        bs = ', '.join(list(map(str, b))) 
        if bs in B:
            if p1:
                return cycles
            return cycles - list(B).index(bs)
        B.add(bs)
        cycles += 1


print(solve(True))
print(solve(False))
