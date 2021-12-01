def get_data():
    with open('data.in', 'r') as f:
        L = [(l.strip()[0], int(l.strip()[1:])) for l in f]
    return L

def part_1():
    L = get_data()
    x, y = 0, 0
    #N and E are +
    direction = 1 #start facing E
    #direction can be 0, 1, 2, 3
    #where North, East, South, West
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for  cmd, val in L:#iterate through the list of tuples
        if cmd == 'N':
            #move north by given value
            y += val
        elif cmd == 'S':
            y -= val
        elif cmd == 'E':
            x += val
        elif cmd == 'W':
            x -= val
        elif cmd == 'L':
            #direction = current directiom
            for _ in range(val//90):
                direction = (direction+3)%4 
        elif cmd == 'R': 
            for _ in range(val//90):
                direction = (direction+1)%4
        elif cmd == 'F':
            x += dx[direction]*val
            y += dy[direction]*val
        else:
            assert False
    return abs(x)+abs(y)

def part_2():
    L = get_data()
    #N and E are +
    #ship pos
    x, y, = 0, 0
    #wp
    wx, wy = 10, 1
    #if ship moves, wp moves by same amt
    for cmd, val in L:
        if cmd == 'N':
            wy += val
        elif cmd == 'S':
            wy -= val
        elif cmd == 'E':
            wx += val
        elif cmd == 'W':
            wx -= val
        elif cmd == 'L':
            #rotate waypoint around ship anti clockwise by VAL degrees
            for _ in range(val//90):
                wx, wy = -wy,wx
        elif cmd == 'R':
            for _ in range(val//90):
                wx, wy = wy, -wx
        elif cmd == 'F':
            y += wy*val
            x += wx*val
        else:
            assert False
    return abs(x) + abs(y)

print(part_1())
print(part_2())
