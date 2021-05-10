#circuit description as dictionary

with open('data.in', 'r') as f:
    C = {l.strip()[l.index('->')+3:]: l[:l.index('->')-1] for l in f}
    #cmd, num wires, out
    print(C)

