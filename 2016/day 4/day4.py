from string import ascii_lowercase as al

def get_data():
    with open('data.in', 'r') as f:
        L = [l.strip().split('-') for l in f]
    return L

def solve(p1):
    L = get_data()
    ans = 0
    for l in L:
        count = {}
        sector_id = int(l[-1][:l[-1].index('[')])
        checksum = l[-1][l[-1].index('[')+1:-1]
        chars = ''.join(l[:-1])
        if p1:
            count = {char : chars.count(char) for char in sorted(chars) if char not in count}
            c = sorted(count, key=count.get, reverse=True)
            if ''.join(list(c)[:5]) == checksum:
                ans += sector_id
        else:
             plaintext = ''.join([al[int(al.index(char)+sector_id)%26] for char in chars])
             if plaintext == 'northpoleobjectstorage':
                 ans = sector_id
    return ans


print(solve(True))
print(solve(False))
