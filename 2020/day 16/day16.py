def get_data():
    with open('data.in', 'r') as f:
        data = [i.strip() for i in f]
    return data


def get_valid_ranges(data):
    #format data into different vars so it looks all sexy
    #37-594 or 615-952
    valid_ranges = {} #valid ranges
    #for i in data[:20]:
    #print(i)
    for d in data[:data.index('')]:
        #print(d)
        l1 = d[d.index(':')+2 : d.index('-')]
        u1 = d[d.index('-')+1:d.index(' or ')]
        l2 = d[d.index(' or ')+4 : len(d)-d[::-1].index('-')-1]
        u2 = d.strip()[len(d)-d[::-1].index('-'):] 
        #departure location info
        ranges = [(int(l1), int(u1)), (int(l2), int(u2))]
        valid_ranges[d[:d.index(':'):]] = ranges
    #print(valid_ranges)
    return valid_ranges

def get_invalid_nums(valid_ranges, num): #runs for each line of the nearby tickets
    valid = False
    for i, k in enumerate(valid_ranges.items()):
        l1, u1 = k[1][0]
        l2, u2 = k[1][1]
        #doesnt have to be invalid for all, just at least one
        if int(l1)<=int(num)<=int(u1) or int(l2)<=int(num)<=int(u2):
            # if valid
            valid = True
    return valid

def part_1():
    data = get_data()
    valid_ranges = get_valid_ranges(data)
    #now go through data and find invalids
    tser = [] #ticket scan error rate
    for line in data[len(data)-data[::-1].index('')+1:]:
        for index, num in enumerate(line.split(',')):
            #if l1<=num<=u1 or l2<=num<=u2
            #for each num in the line, check if it is valid
            valid = get_invalid_nums(valid_ranges, num)
            if not valid:
                tser.append(int(num))
    return sum(tser)

#runs for each col
def test_range(col, ranges): #ranges = [(l1, u1), (l2, u2)]
    l1, u1 = ranges[0]
    l2, u2 = ranges[1]
    valid = 0
    for num in col:
        if int(l1)<=int(num)<=int(u1) or int(l2)<=int(num)<=int(u2):
            valid += 1
            #print(f'{num} works for range {ranges}')
        #else:
            #print(f'{num} doesnt work for range {ranges}')
    if valid == len(col):#if all the numbers in the col are valid
        return True
    else:
        return False
#print(part_1()) 
data = get_data()
#identify tickets that have an invalid value and discard them
data = get_data()
valid_ranges = get_valid_ranges(data)
print(valid_ranges)
print(len(valid_ranges))
valid_data = []
for line in data[len(data)-data[::-1].index('')+1:]:
    is_line_valid = True
    for index, num in enumerate(line.split(',')):
        #if l1<=num<=u1 or l2<=num<=u2
        #for each num in the line, check if it is valid
        valid = get_invalid_nums(valid_ranges, num)
        if not valid:
            is_line_valid = False
    if is_line_valid:
        valid_data.append(line)
#find max and min for each number
#now we have a grid of valid data, where cols are of the same type
#print(valid_data)
for key, val in valid_ranges.items():
    print(key, val)
R = len(valid_data)
C = len(valid_data[0].split(','))

names = set()
for name in valid_ranges.keys():
    if name not in names:
        names.add(name)
mapping = {} #  col_no : possible col names
used = set()
could_be = {c: set(names) for c in range(C)}
print(could_be)
"""
for c in range(C):
    mapping[c] = set()
    col_data = [int(i.split(',')[c]) for i in valid_data]
    #print(sorted(col_data))
    for name, ranges in valid_ranges.items():
        #print(name)
        #for each range
        #check if range is valid
        if test_range(col_data, ranges) and name in names and len(mapping[c]) == 0:
            mapping[c].add(name) #is add right?
            names.remove(name)
            print(f'mapped {name} to {c}')
"""
while len(mapping) <= 20: #or equal to?
    for c in range(C):
        col_data = [int(i.split(',')[c]) for i in valid_data]
        possible = [name for name in could_be[c] if name not in used and test_range(col_data, ranges) == True]
        if len(possible) == 1:
            mapping[i] = possible[0]
            used.add(possible[0])    
#print("="*80)
#print(mapping)
#for k,v in mapping.items():
#    print(k,v)
#print(names)
#now caluclate values for my ticket
mine = [11,12,13]

"""
#print col 1, col 2
#print(valid_data)
print("="*80)
for line in valid_data:
    line = line.split(',')
    print(line[0], line[1]) 
    #max_, min_ = max([i.split(',')[c] for i in valid_data]), min([i.split(',')[c] for i in valid_data])
    #print(min_, max_)
"""



    

