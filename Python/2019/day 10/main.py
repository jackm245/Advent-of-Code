import sys

def get_data():
    with open(sys.argv[1], 'r') as f:
        L = [l.strip() for l in f]
    return L


L = get_data()
print(L)
