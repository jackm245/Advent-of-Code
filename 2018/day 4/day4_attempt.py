from pprint import pprint as p
import collections
import re
#step 1: arrange data in chronological order
#arrange by month, day, and tehn minute
with open('data.in', 'r') as f:
    d = {l[l.index('[')+1:l.index(']')] : l[l.index(']')+2:-1] for l in f}#date, action
    data = collections.OrderedDict(sorted(d.items()))
with open('data.in', 'r') as f:
    times = sorted([l[l.index('[')+1:l.index(']')] for l in f])

print(times)
print(data)
p(data)
sleep = {} #guard id : time asleep

#find guard with most minutes asleep
#for each day/night find time asleep and add up
for date, action in data.items():
    if action.startswith('Guard'):
        ID = int(re.findall(r'\d+', action)[0])
        #print(ID)
        if ID not in sleep:
           sleep[ID] = 0
        wake_time = date[-5:]
        if wake_time.startswith('00'):
            start_minute = wake_time[-2:]
        else:
            start_minute = '00'
        print(wake_time, start_minute)
    #elif action.startswith('falls)
    #find mins asleep
#add to dict
#find one with most mins asleep
