from itertools import cycle
from copy import deepcopy

def rotate(l, n):
    return l[n:] + l[:n]
def get_data():
    with open('data.in') as f:
        C = [int(l) for l in f.readline().strip()]
        #original list of all cups 1-8
        return C
# = current cup
def solve(C, moves, p1): #cups, moves
    length = len(C)
    c = C[0]
    for n in range(moves): #100 moves
        #print(f'-- move {n+1} --')
        index = n % length
        ni = (n+1)%length
        cc = C[index]
        #print(cc)
        #print(C)    
        #The crab picks up the three cups that are immediately clockwise of the current cup. 
        #They are removed from the circle
        removed = []
        #idx = index + addr
        remove_idx = ni
        for _ in range(3):
            removed.append(C[remove_idx])
            remove_idx = (remove_idx+1)%length
        #print(removed)
        C = [i for i in C if i not in removed]
        next_c = C[((C.index(cc))+1)%(len(C))] #wrong?
        #The crab selects a destination cup:
        i = cc-1 #he cup with a label equal to the current cup's label minus one
        #destination = cup number
        while 1:
            if i < min(C):
                i = max(C)
            if i in C:
                dc = i
                #destination found =  i
                break
            i -= 1
        #print(dc)
        #The crab places the cups it just picked up so that they are 
        #immediately clockwise of the destination cup
        new_C = C[:C.index(dc)+1] #from beginning -> designated
        new_C.extend(removed) #new cups
        new_C.extend(C[C.index(dc)+1:])#rest of cups
        #now rotate list so it is correct order
        #print(f'next: {next_c}')
        while new_C[ni] != next_c:
            new_C = rotate(new_C, 1)
        C = deepcopy(new_C)
       # print('\n')
    # now get order after cup 1
    cao = []
    cao.extend(C[C.index(1):])
    cao.extend(C[:C.index(1)])
    if p1:
        return ''.join([str(i) for i in cao][1:])
    else:
        print(cao[:10])
        print(f'{cao[1]} * {cao[2]}')
        return cao[1] * cao[2]

def part_1():
    cups = get_data()
    return solve(cups, 100, True)

def part_2():
    cups = get_data()
    cups.extend(int(i) for i in range(max(cups)+1, 1000001)) #to 1 million and 1 = 1000001
    moves = 10000000 # = 10 million
    return solve(cups, moves, False)

print(part_1())
print(part_2())
