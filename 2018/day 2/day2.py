with open('data.in', 'r') as f:
    L = [l.strip() for l in f]

def part_1():
    ans = 0
    two = 0
    three = 0
    for l in L:
        counts = [l.count(char) for char in l]
        if 2 in counts:
            two += 1
        if 3 in counts:
            three += 1

    return two * three


#find the correct boox ids first
#these will differ by exactly 1 character
def part_2():
    for x in L:
        for y in L:
            diff = sum([1 for i in range(len(x)) if x[i] != y[i]])
            if diff == 1:
                ans = [x[i] for i in range(len(x)) if x[i] == y[i]]
                return ''.join(ans)


print(part_1())
print(part_2())

