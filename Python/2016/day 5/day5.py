import hashlib


def part_1():
    password = []
    i = 0
    while 1:
        string = 'uqwqemis'+str(i)
        result = str(hashlib.md5(string.encode()).hexdigest())
        if result.startswith('00000'):
            password.append(result[5])
            print(password)
        if len(password) == 8:
            return ''.join(password)
        i += 1

def part_2():
    password = ['_' for _ in range(8)]
    i = 0
    while 1:
        string = 'uqwqemis'+str(i)
        #string = 'abc'+str(i)
        result = str(hashlib.md5(string.encode()).hexdigest())
        if result.startswith('00000'):
            pos = result[5] #indexing starts at 0
            val = result[6]
            try:
                pos = int(pos)
                password[pos]
            except:
                pass
            else:
                if password[pos] == '_':
                    password[pos] = val
            print(password)
        if '_' not in password:
            return ''.join(password)
        i += 1

print(part_1())
print(part2())
