with open('data.in', 'r') as f:
    data = [int(i) for i in f.readline().strip().split(',')]
last_index = {}
for i, n in enumerate(data):
    if i != len(data)-1:
        last_index[n] = i
while len(data) < 30000000:
    prev = data[-1] #last number spoken
    prev_prev = last_index.get(prev, -1)
    last_index[prev] = len(data)-1
    if prev_prev == -1:
        #if it had only been spoken once
        next_num = 0#
    else:
        #if lns had been spoken before
        next_num = len(data) - 1 - prev_prev
    data.append(next_num)
    if len(data) == 2020:
        print(data[-1])
print(data[-1])
