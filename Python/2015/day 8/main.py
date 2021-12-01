import sys
from curses import ascii as a

def get_data():
    with open(sys.argv[1], 'r') as f:
        L = [l.strip() for l in f]
    return L


def part_one(L):
    return (sum([len(l) - len(eval(l)) for l in L]))




def part_two(L):
    return (sum([2+l.count('\\') + l.count('"') for l in L]))


L = get_data()
print(part_one(L))
print(part_two(L))
