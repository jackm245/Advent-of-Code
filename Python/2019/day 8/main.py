"Advent of Code 2019 Day 8"


def get_data(filename):
    with open(filename, 'r') as file:
        F = [int(digit) for digit in file.readline().strip()]
        D = [[F[i+(j*WIDE):i+((j+1)*WIDE)] for j in range(0, TALL)] for i in range(0, len(F), WIDE*TALL)]
        return D


def part_one(D):
    lowest = (100,-1)
    for n, layer in enumerate(D):
        # lowerst (0's, index)
        number_of_zeroes = sum([i.count(0) for i in layer])
        if number_of_zeroes < lowest[0]:
            lowest = (number_of_zeroes, n)
    return sum([i.count(1) for i in D[lowest[1]]]) * sum([i.count(2) for i in D[lowest[1]]])


def part_two(D):
    # 100 layers
    # each layer has 25 numbers per row
    # each layer has 6 rows
    final = [['_' for _ in range(WIDE)] for _ in range(TALL)]
    for row in range(TALL):
        for column in range(WIDE):
            for layer in range(len(D)):
                char = D[layer][row][column]
                if char != 2 and final[row][column] == '_':
                    final[row][column] = char
    for i in final:
        a = ''.join(list(map(str, i)))
        a = a.replace('1', '#')
        a = a.replace('0', '.')
        print(a)
        # first check the first character of the first row of teh first layer
        # then first character of first row of second layer until character != 2. Thats the final one
        # the second character of first row of first layer
        # the second characvter of second row of second layer

        # the end picture will be WIDE x TALL


WIDE = 25
TALL = 6
D = get_data("input.txt")
print(part_one(D))
part_two(D)
