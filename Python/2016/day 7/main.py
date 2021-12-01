import sys
import re

def get_data():
    with open(sys.argv[1], 'r') as f:
        L = [l.strip() for l in f]
        S = [re.split(r'\[|\]', l) for l in L]
    return S


def part_one(L):
    count = 0
    for l in L:
        #  print('l', l)
        line_true = []
        for x, i in enumerate(l):
            #  print('i', i)
            sub_true = []
            for n in range(len(i)):
                # i is the sub string in the line
                #  print('n, l', n, j)
                try:
                    #  print(i[n], i[n+1], i[n+2], i[n+3])
                    if (i[n] != i[n+1]) and (i[n] ,i[n+1]) == (i[n+3], i[n+2]):
                        sub_true.append(True)
                    #  else: # could get rid of potentially
                        #  sub_true.append(False)
                except IndexError:
                    #  print('index error')
                    continue
            #  print(i, any(sub_true))
            # evens are out of brackets
            # odds are in brackets
            # assuming line doesnt start with bracket
            has_four = any(sub_true)
            if x % 2 == 0:
                if has_four:
                    line_true.append(True)
                # if not have a four outisde bracket, entire row bad
            else:
                # for a str in the bracket
                # if has a four, then enitre row False
                # if has not a four, then this section ok
                # return false if has 4 in bracket and true if has one outside bracket
                if has_four:
                    line_true.append(False)
                #  line_true.append(not(any(sub_true)))
        if all(line_true) and len(line_true) != 0:
            count += 1
    return count




def part_two(L):
    # one list for outside brackets
    # one for inside bracklets
    # is all inside brackets found in outside bracklets
    count = 0
    for l in L:
        #  print(l)
        supernet_sequences = [a for x, a in enumerate(l) if x % 2 == 0] # outside square brackets
        hypernet_sequences = [a for x, a in enumerate(l) if x % 2 == 1] # inside square brackets
        # find a BAB in on the the hypoernet hypernet_sequences
        ABAs = []
        for h in hypernet_sequences:
            #  print(f'h {h}')
            for n  in range(len(h)):
                try:
                    if h[n] == h[n+2] and h[n] != h[n+1]:
                        ABAs.append(''.join([h[n+1], h[n], h[n+1]]))
                except IndexError:
                    continue
        #  print(ABAs)
        if any([any([i in j for j in supernet_sequences]) for i in ABAs]):
            count += 1
    return count


L = get_data()
#  print(L)
print(f'part one: {part_one(L)}')
print(f'part two: {part_two(L)}')
