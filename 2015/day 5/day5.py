import re

with open('data.in', 'r') as f:
    L = [l.strip() for l in f]

nice = []

for string in L:
    if re.search(r'(\w*[aeuio]\w*){3,}', string) and re.search(r'(\w)\1', string) and re.search(r'(ab|cd|pq|xy)', string) is None:
        nice.append(string)

print(len(nice))

rly_nice = []
for string in L:
    if re.search(r'([a-z]{2}).*\1', string) and re.search(r'([a-z]).\1', string):
        rly_nice.append(string)
print(len(rly_nice))
