with open('data.in', 'r') as f:
    k1, k2 = (int(l.strip()) for l in f)

def transform(n, ls):
    return pow(n, ls, 20201227)


l1 = 0
while transform(7, l1) != k1:
    l1 += 1

l2 = 0
while transform(7, l2) != k2:
    l2 += 1

encryption = transform(k1, l2)
print(encryption)


