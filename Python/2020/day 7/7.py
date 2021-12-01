outer_bag_colors = set()


def main():
    global outer_bag_colors
    p1 = 0
    p2 = 0
    try:
        with open('7.in', 'r') as fin:
            data = fin.read().splitlines()
            get_outer_bag_color(data, 'shiny gold')
            p1 = len(outer_bag_colors)
            p2 = get_total_bags_count(data, 'shiny gold')
    finally:
        fin.close()
        print(f'Part 1: {p1}')
        print(f'Part 2: {p2}')


def get_outer_bag_color(data, bag_color):
    global outer_bag_colors
    for line in data:
        o, i = line.split('contain ')
        oc = o.split(' bags')[0]
        if bag_color in i:
            outer_bag_colors.add(oc)
            get_outer_bag_color(data, oc)


def get_total_bags_count(data, bag_color):
    count = 0
    for line in data:
        outer_bag, inner_bags = line.split('contain ')
        outer_bag_color = outer_bag.split(' bags')[0]
        if bag_color == outer_bag_color and 'no other bags' not in inner_bags:
            inner_bags_list = inner_bags.split(', ')
            count = sum([int(x.split(' ')[0]) for x in inner_bags_list])
            for inner_bag in inner_bags_list:
                bag_count = int(inner_bag.split(' ')[0])
                inner_bag_color = inner_bag.split(' bag')[0][2:]
                count += bag_count * get_total_bags_count(data, inner_bag_color)
    return count


if __name__ == '__main__':
    main()
