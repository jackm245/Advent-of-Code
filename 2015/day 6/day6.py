import re

def get_data():
    with open('data.in', 'r') as f:
        L = [l for l in f]
#toggle = not(pos)
#turn off = pos=False
#turn on = pos=True
#data = list of  (keyword, (startx, y), (endx, y))
    data = []
    for line in L:
        if line.startswith('toggle'):
            keyword = 'toggle'
        elif line.startswith('turn on'):
            keyword = 'on'
        elif line.startswith('turn off'):
            keyword = 'off'
        else:
            assert False
        ints = re.findall('-?\d+', line)
        startx, starty, endx, endy = ints
        data.append((keyword, int(startx), int(starty), int(endx), int(endy)))
    return data

def part_1():
    data = get_data()
    C, R = 1000, 1000
    grid = [[False for _ in range(C)]for _ in range(R)]
    for kw, startx, starty, endx, endy in data:
        for r in range(starty, endy+1):
            for c in range(startx, endx+1):
                if kw == 'toggle':
                    grid[r][c] = not(grid[r][c])
                elif kw == 'on':
                    grid[r][c] = True
                elif kw == 'off':
                    grid[r][c] = False
                else:
                    assert False 
            # the number row to start on
            # position on row
    ans = 0
    for row in grid:
        for light in row:
            if light:
                ans += 1
    return ans

#398,967 too low
def part_2():
    data = get_data()
    C, R = 1000, 1000
    grid = [[0 for _ in range(C)] for _ in range(R)]

    for kw, startx, starty, endx, endy in data:
        for r in range(starty, endy+1):
            for c in range(startx, endx+1):
                if kw == 'toggle':
                    grid[r][c] = grid[r][c]+2
                elif kw == 'on':
                    grid[r][c] = grid[r][c]+1
                elif kw == 'off':
                    grid[r][c] = grid[r][c]-1
                    if grid[r][c] < 0:
                        grid[r][c] = 0
                else:
                    assert False 
    ans = 0
    for row in grid:
        for light in row:
            ans += light
    return ans

print(part_1())
print(part_2())
