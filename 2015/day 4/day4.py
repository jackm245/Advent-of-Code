import hashlib
import re

def get_data():
    with open('data.in', 'r') as f:
        L = [i.strip() for i in f.readline().strip()]
    return L

def solve(p1):
    L = get_data()
    i = 0
    while True:
        key = ''.join(L) + str(i)
        result =  hashlib.md5(key.encode()).hexdigest()
        if re.match('^00000', result) is not None and p1:
            return i
        elif re.match('^000000', result) is not None and not p1:
            return i
        else:
            i += 1

print(solve(True))
print(solve(False))
