import fileinput
from functools import reduce
#use ones with just one allergen to find out what they are
#allegern {}  english : foreign 
allergens_dict = {}
with open('data.in', 'r') as f:
    data = []
    allergens = set() #set of allerggems
    for line in f:
        l_ingredients = [i for i in line.split(' ')[:line.split(' ').index('(contains')]]
        l_allergens = [i[:-1]for i in line.strip().split(' ')[line.split(' ').index('(contains')+1:]]
        data.append((l_ingredients, l_allergens))
        for a in l_allergens:
            allergens.add(a)
#iterate through each allergen. If there are lines with it just in once. Compare and get ans
length = len(data)
#print(allergens)
for a in allergens:
    #get all lines where there is just the one allergen
    lines = [set(j for j in i[0]) for i in data if len(i[1]) == 1 and i[1][0] == a]
    #for line in lines:
    #print(line) #line has 1 allergen and that is wheat
    try:
        ingredients_that_contain_a = list(reduce(set.intersection, [set(item) for item in lines]))
    except TypeError: #if a isnt one its own at all
        continue
    else:
        allergens_dict[a] = ingredients_that_contain_a
#print(allergens)
#print(allergens_dict)
#print(len(allergens))
#print(len(allergens_dict))
print(allergens_dict.keys())
#now loop back through, to find allergens that do not appear once on a line
#for every allergens not yet found
#for every line that contains that allergen
#find the common intersection
#remove from intersection any found allergens alrady
#we have our newly found allergen
#print(data)

"""
unfound_allergens = [i for i in allergens if i not in allergens_dict]
for ua in unfound_allergens:
    print(ua)
    #find every line that contains this ua
    lines_that_contain_ua = []
    for line in data:
        #print(data[1])
        if ua in line[1]:
            lines_that_contain_ua.append(line[0])
    #print(lines_that_contain_ua)
    #find intersections between these lines
    da = list(reduce(set.intersection, [set(item) for item in lines_that_contain_ua]))[0]
    #NEED TO REMOVE ALREADY FOUND ALLERGENS
    print(da)
#print(allergens_dict)
"""
