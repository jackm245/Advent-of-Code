import re

with open('data.in', 'r') as f:
    L = [list(map(int, re.findall(r'\d+', l))) for l in f]

def solve(p1):
    ans = 0
    for l in L:
        if p1:
            ans += max(l) - min(l)
        else:
            for a in l:
                for b in l:
                    if a != b and a % b == 0:
                        ans += a // b 
    return ans

print(solve(True))
print(solve(False))
