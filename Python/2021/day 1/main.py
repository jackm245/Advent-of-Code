import sys

def get_data():
    with open(sys.argv[1], 'r') as f:
        L = [int(l.strip()) for l in f]
    return L


def part_one(L):
    count = sum([1 for i in range(len(L)-1) if L[i+1] > L[i]])
    return count

def part_two(L):
    count = sum([1 for i in range(len(L)-1) if sum(L[i : i + 3]) < sum(L[i + 1 : i + 4])])
    return count

L = get_data()
print(f'part one: {part_one(L)}')
print(f'part two: {part_two(L)}')

print('1832, 1858')
