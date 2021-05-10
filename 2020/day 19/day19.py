from copy import deepcopy
import re
with open('data.in', 'r') as f:
    L = [l.strip() for l in f]
#print(L)
r = L[:L.index('')]
M = L[L.index('')+1:]
#print(r, m)

R = {}
for i in sorted(r):
    index = i.index(':')
    i2 = i.index(':')+2
    if i[i2:] == '\"a\"' or i[i2:] == '\"b\"':
        val = i[i2:][1:-1]
    else:
        val = i[i2:]
    key = int(i[:index])
    R[key] = val
#print(R)

#ditionary of rules
#rule number : regex for rule

rules = {}
#recursive function to put the rules list in terms of A and B
fr = [i for i in R[0] if i!= ' '] #first rule
print(fr)
while any([i.isdigit() for i in fr]):#while there is a digit in the str
    new_rule = []
    for idx, char in enumerate(fr):
        if not char.isdigit():
            new_rule.append(char)
        else:
            replacement = [i for i in R[int(char)] if i != ' ']
            new_rule.append('(')
            new_rule.extend(replacement)
            new_rule.append(')')
    fr = deepcopy(new_rule)
    #print(fr)
rl = ['^']
rl.extend(fr)
rl.append('$')
rule = ''.join(rl)
ans = 0
for msg in M:
    if re.match(rule, msg) is not None:
        ans+=1
print(ans)



#rules dict and messages list
#for each message in list:
# if matches rule 0:
#ans+=1
 
