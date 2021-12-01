def get_data(filename):
    with open(filename, 'r') as f:
        O = [l.strip().split(')') for l in f]
    return O

def f(x, orbits_dict):
    ans = 0
    for y in orbits_dict[x]:
        ans += f(y, orbits_dict)+1
    return ans

def part_one(O):
    # make a dictionary with all of the planets that have other planets orbitting them as keys
    # then the values are the planets that orbit that planets
    orbits_dict = {}
    for primary, secondary in O:
        if primary in orbits_dict:
            orbits_dict[primary] += secondary
        else:
            orbits_dict[primary] = secondary
    ans = 0
    for x in orbits_dict:
        ans += f(x, orbits_dict)
    print(ans)

data = get_data('data.in')
part_one(data)

