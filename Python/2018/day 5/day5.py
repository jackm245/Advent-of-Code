from string import ascii_lowercase as alpha
from copy import deepcopy


with open('data.in', 'r') as f:
    W = [l for l in f.readline()][:-1]

def react(W):
    while True:
        changes = 0
        for i in range(len(W)-1):
            #print(W)
            # print(W[i])
            #print(W[i+1])
            try:
                W[i]
                W[i+1]
            except IndexError:
                continue
            else:
                if W[i].lower() == W[i+1].lower():
                    if (W[i].isupper() and W[i+1].islower()) or (W[i].islower() and W[i+1].isupper()):
                        #if Ul or lU and both of same char
                        #get rid
                        #print(W[i])
                        del W[i]
                        #print(W[i])
                        del W[i]
                        changes += 1
        if changes == 0:
            return W
#print(len(W))
#print(W)

#print(react([i for i in 'dabAcCaCBAcCcaDA']))
#irint(react(W)) -> part 1

def part_1():
    return len(react(W))

def part_2():
#reduce for each letter in the alphabet
#W = [l for l in 'dabAcCaCBAcCcaDA']
    shortest = None
    for char in alpha:
        l = deepcopy(W)
        if char in l:
            while char in l:
                l.remove(char)
            while char.upper() in l:
                l.remove(char.upper())
            r = react(l)
            #print(f'{char} : {len(r)}')
            if shortest is None or len(r) < shortest:
                shortest = len(r)
    return shortest

print(part_1())
print(part_2())
