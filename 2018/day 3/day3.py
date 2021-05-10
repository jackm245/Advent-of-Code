import re


def get_claim_coords(claim): 
    tx = claim[1]
    ty = claim[2]
    width = claim[3]
    height = claim[4]
    coords = [(tx+w, ty+h) for w in range(width) for h in range(height)]
    return coords


with open('data.in', 'r') as f:
    L = [list(map(int, re.findall(r'\d+', l))) for l in f]

def solve(p1):
    claimed = {} #(x, y) : count
    for l in L:
        #print("="*80)
        coords = get_claim_coords(l)
        #print(l, coords)
        for coord in coords:
            if coord in claimed.keys():
                claimed[coord] += 1
            else:
                claimed[coord] = 1

    if p1:
        ans = 0
        for (x, y), count in claimed.items():
            if count > 1:
                ans += 1
        return ans
    else:
        for l in L:
            coords = get_claim_coords(l)
            if all([claimed[i] == 1 for i in coords]):
                return l[0]

print(solve(True))
print(solve(False))

