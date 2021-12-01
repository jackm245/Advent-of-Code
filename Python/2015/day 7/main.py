import sys


def calculate(name):
    try:
        return int(name)
    except ValueError:
        pass

    if name not in results:
        ops = calc[name]
        if len(ops) == 1:
            res = calculate(ops[0])
        else:
            op = ops[-2]
            if op == 'AND':
              res = calculate(ops[0]) & calculate(ops[2])
            elif op == 'OR':
              res = calculate(ops[0]) | calculate(ops[2])
            elif op == 'NOT':
              res = ~calculate(ops[1]) & 0xffff
            elif op == 'RSHIFT':
              res = calculate(ops[0]) >> calculate(ops[2])
            elif op == 'LSHIFT':
              res = calculate(ops[0]) << calculate(ops[2])
        results[name] = res
    return results[name]



calc = dict()
results = dict()
with open(sys.argv[1], 'r') as f:
    commands = [l for l in f]


for command in commands:
    (ops, res) = command.split('->')
    calc[res.strip()] = ops.strip().split(' ')


one = calculate('a')
print(f'part one: {one}')
results = dict()
results['b'] = one
two = calculate('a')
print(f'part two: {two}')
