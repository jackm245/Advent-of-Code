import collections

with open('data.in', 'r') as f:
    L = [l.strip() for l in f]
    
cols = [[] for _ in range(len(L[0]))]
for l in L:
    for i, char in enumerate(l):
        cols[i].append(char)

for c in cols:
    print(collections.Counter(c).most_common()[0][0], end="")

for c in cols:
    print(collections.Counter(c).most_common()[-1][0], end="")
