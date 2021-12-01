#day10_jp.py


def get_data():
    with open('data.in', 'r') as f:
        data = [int(line.strip()) for line in f]
        data.append(0)
        sd = sorted(data)
        sd.append(max(sd)+3)
        return sd

def part_1():
    sd = get_data()
    n1 = 0
    n3 = 0
    for i in range(len(sd)-1):
        d = sd[i+1]-sd[i]
        if d == 1:
            n1+=1
        elif d == 3:
            n3+=1
    print(n1 * n3)


def part_2():
    sd = get_data()
    DP = {}
    def dp(i):
        if i == len(sd)-1:
            return 1
        if i in DP:
            return DP[i]
        ans = 0
        for j in range(i+1, len(sd)):
            if sd[j]-sd[i]<=3:
                ans+= dp(j)
        DP[i] = ans
        return ans
    print(dp(0))


part_1()
part_2()
