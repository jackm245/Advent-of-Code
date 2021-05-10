#use ones with just one allergen to find out what they are
#allegern {}  english : foreign


def get_data(): 
    all_A = set()
    all_I = set()
    with open('data.in', 'r') as f:
        data = []
        for line in f:
            l_ingredients = [i for i in line.split(' ')[:line.split(' ').index('(contains')]]
            for i in l_ingredients:
                all_I.add(i)
            l_allergens = [i[:-1]for i in line.strip().split(' ')[line.split(' ').index('(contains')+1:]]
            for i in l_allergens:
                all_A.add(i)
            data.append((l_ingredients, l_allergens))
    could_be = {i: set(all_A) for i in all_I}
    for food in data:
        #remove all ingredients not on that list for the two allergens
        I = food[0]
        A = food[1]
        for a in A:
            for i in all_I:
                if i not in I:
                    could_be[i].discard(a)
    return all_A, all_I, data, could_be


#print(all_I)


#for each allergen, the ingredients that are not on that line, can not be the allergen
#we start by assuming that each ingreditn could be an allergen
def part_1():
    all_A, all_I, data, could_be = get_data()
    p1 = 0
    for food in data:
        for i in all_I:
            if not could_be[i]:
                p1 += food[0].count(i)
    return p1


def part_2():
    all_A, all_I, data, could_be = get_data()
    MAPPING = {}
    USED = set()
    while len(MAPPING) < len(all_A):
        for i in all_I:
            possible = [a for a in could_be[i] if a not in USED]
            if len(possible) == 1:
                MAPPING[i] = possible[0]
                USED.add(possible[0])

    p2 = ','.join([k for k, v in sorted(MAPPING.items(), key=lambda kv:kv[1])])
    return p2

print(part_1())
print(part_2())
