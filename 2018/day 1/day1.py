with open('data.in', 'r') as f:
    L = [int(l.strip()) for l in f]

def solve(p1):
    freqs = set()
    ans = 0
    while True:
        for l in L:
            ans += l
            if ans in freqs:
                return ans
            else:
                freqs.add(ans)
        if p1:
            return ans
        #print(ans)

print(solve(True))
print(solve(False))
