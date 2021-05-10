def get_data():
    with open('data.in', 'r') as f:
        L = [l.strip().split(' ') for l in f]
    return L


def has_duplicates(arr):
    count = {w : arr.count(w) for w in arr}
    #print(count)
    for key, val in count.items():
        if val != 1:
            return True
    return False


def solve(p1):
    L = get_data()
    ans = 0
    for l in L:
        if not p1:
            l = [''.join(sorted(w)) for w in l]
        ans += int(not(has_duplicates(l)))
    return ans

print(solve(True))
print(solve(False))
    


