def get_data(filename):
    with open(filename, 'r') as f:
        R = list(map(int, f.readline().split('-')))
        return R


def part_one(R):
    pwds = []
    for i in range(R[0], R[1]+1):
        # check that i is always increasing
        s = [x for x in str(i)]
        if s[0] <= s[1] <= s[2] <= s[3] <= s[4] <= s[5]:
            # check that there is a repeating digit
            r = False
            for j in range(len(s)-1):
                if s[j] == s[j+1]:
                    r = True
                    break
            if r:
                pwds.append(i)
    return pwds


def part_two(R):
    P = list(map(str, part_one(R)))
    pwds = []
    for p in P:
        C = [p.count(str(i)) for i in set(p)]
        if 2 in C:
            pwds.append(p)
    return len(pwds)


R = get_data('data.in')
print(len(part_one(R)))
print(part_two(R))
