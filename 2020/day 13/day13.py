def get_data_p1():
    with open('data.in', 'r') as f:
        timestamp =int( f.readline())
        buses = [int(i) for i in f.readlines()[0].strip().split(',') if i != 'x']
        return timestamp, buses


def get_data_p2():
    with open('data.in', 'r') as f:
        data = f.readlines()[1].strip().split(',')
    B = [(int(bus), i) for i, bus in enumerate(data) if bus != 'x']
    return B


def part_1():
    timestamp, buses = get_data_p1()
    best = None
    start_time = timestamp
    for bus in buses:
        t = start_time
        while t % bus != 0:
            t+=1
        wait_time = t - start_time
        if best is None or wait_time < best[0]:
            best = (wait_time, bus)
    return best[0]*best[1]

def part_2():
    B = get_data_p2()
    lcm = 1
    ans = 0    
    for i in range(len(B)-1):
        bus_id = B[i+1][0]
        idx = B[i+1][1]
        lcm *= B[i][0]
        while (ans + idx) % bus_id != 0:
            ans += lcm
    return ans


print(part_1())
print(part_2())
