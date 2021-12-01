import sys
import re

def get_data():
    with open(sys.argv[1], 'r') as f:
        L = [l.strip() for l in f]
    return L


def part_one(L):
    count = 0
    for l in L:
        S = l.split()
        print(S)
        nums = list(map(int, re.findall(r'\d+', S[0])))
        c = S[1][0]
        s = S[-1]
        if nums[0] <= s.count(c) <= nums[1]:
            count += 1
    return count
        #  if s.count()



def part_two(L):
    count = 0
    for l in L:
        S = l.split()
        print(S)
        nums = list(map(int, re.findall(r'\d+', S[0])))
        c = S[1][0]
        s = S[-1]
        a = 0
        if s[nums[0]-1] == c:
            a+= 1
        if s[nums[1]-1] == c:
            a += 1
        if a == 1:
            count += 1
    return count


L = get_data()
#  print(L)
print(f'part one: {part_one(L)}')
print(f'part two: {part_two(L)}')
