from math import sqrt

#part 1 works for my input but not for all :)
input_ = 277678
#num=22
num = input_
x, y = 0, 0
i = 0
n=0
while 1:
    if (i*i) % 2 == 1:
        if (i*i) >= num:
            largest = i*i
            print(i)
            break
        else:
            n+=1
    i += 1
print(largest)
row_len = sqrt(largest)
bot_r = largest
bot_l = int(largest-row_len+1) #the bottom left number
top_l = int(bot_l-row_len+1)
top_r = int(top_l-row_len+1)
print(bot_r, bot_l, top_l, top_r)
mid_bot = int((bot_r+bot_l)//2) #middle of bottom row of grid
print(mid_bot)
if num >= bot_l:#if number is on the bottom row
    x = abs(num-mid_bot) #To make for all inputs, add if statement to cover if number is in each of the outer rows/cols

    y = abs(n) 
print(x, y)
print(x+y) 

def part_2(goal):
    coords = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
    x = y = dx = 0
    dy = -1
    grid = {}

    while True:
        total = 0
        for offset in coords:
            ox, oy = offset
            if (x+ox, y+oy) in grid:
                total += grid[(x+ox, y+oy)]
        if total > int(goal):
            return total
        if (x, y) == (0, 0):
            grid[(0, 0)] = 1
        else:
            grid[(x, y)] = total
        if (x == y) or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy

print(part_2(num))
