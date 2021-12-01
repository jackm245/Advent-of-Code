import re


def get_data():
    with open('data.in', 'r') as f:
        L = [list(map(int, re.findall(r'\d+', l.strip()))) for l in f]
        assert len(L) % 3 == 0
        return L


def is_possible(sides):
    hyp = sides.pop(sides.index(max(sides)))
    if sum(sides) > hyp:
        return True
    else:
        return False


def solve(p1):
    L = get_data()
    valid = 0
    if p1:
        for sides in L:
            valid += int(is_possible(sides))
    else:
        for c in range(3):
            for r in range(0, len(L), 3):
                sides = [L[r][c], L[r+1][c], L[r+2][c]]
                valid += int(is_possible(sides))
    return valid


print(solve(True))
print(solve(False))
