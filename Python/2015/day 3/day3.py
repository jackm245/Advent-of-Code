with open('data.in', 'r') as f:
    data = [j for i in f for j in i][:-2]

houses = []
#up and right are +
sx, sy, rx, ry = 0, 0, 0, 0 #sant xy, robo xy
houses.append((x, y))
for index, i in enumerate(data):
    if index % 2 == 0:
        if i == '^':
            sy += 1
        elif i == 'v':
            sy -= 1
        elif i == '>':
            sx += 1
        elif i == '<':
            sx -= 1
        house = (sx, sy)
        if house not in houses:
            houses.append(house)

    else:
        if i == '^':
            ry += 1
        elif i == 'v':
            ry -= 1
        elif i == '>':
            rx += 1
        elif i == '<':
            rx -= 1
        house = (rx, ry)
        if house not in houses:
            houses.append(house)
print(len(houses))


# 2591 too low

