def get_data():
    with open('data.in', 'r') as data_file:
        data = [1 if i=='(' else -1 for j in data_file for i in j][:-1]
        return data


def part_1():
    data = get_data()
    return sum(data)


def part_2():
    data = get_data()
    total = 0
    for index, number in enumerate(data):
        total += number
        if total < 0:
            return index+1

def main():
    print(part_1())
    print(part_2())

if __name__ == '__main__':
    main()
