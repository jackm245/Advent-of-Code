from copy import deepcopy


def get_data():
    with open('data.in', 'r') as f:
        data = [int(l.strip()) for l in f]
        return data


def solve(p1):
    index = 0
    steps = 0
    L = deepcopy(data)
    while True:
        if index+1 > len(L):
            return steps
        jump = L[index]
        if jump >= 3 and not p1:
            L[index] -= 1
        else:
            L[index] += 1
        index += jump
        steps += 1
        #print (f'step {steps}: from {index-jump} to {index}, change {index-jump}: {jump} -> {L[index-jump]}')


data = get_data()
print(solve(True))
print(solve(False))
