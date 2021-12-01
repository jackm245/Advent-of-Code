def p1_create_group_set(group, new_file):
	group_set = ''.join(sorted(''.join(set(''.join(group)))))
	new_file.append(group_set)
	group = []
	return group, new_file, group_set

def p1_create_data():
	with open('6.in') as raw_file:
		new_file = []
		group = []
		for line in raw_file:
			if line == '\n':
				group, new_file, group_set = p1_create_group_set(group, new_file)
			else:
				group.append(line.strip())
		group, new_file, group_set = p1_create_group_set(group, new_file)
		return new_file

def p1_get_sum_of_counts(grouped_data):
	count = 0
	for group in grouped_data:
		count+=len(group)
	return count

def part_1():
	data = p1_create_data()
	count = p1_get_sum_of_counts(data)
	print(f'part 1: {count}')

def p2_create_group_data(group, new_file):
	chars = [char for char in group[0] if all(char in item for item in group)]
	new_file.append(''.join(chars))
	group = []
	return new_file

def p2_create_data():
	with open('6.in') as raw_file:
		new_file = []
		group = []
		for line in raw_file:
			if line == '\n':
				new_file = p2_create_group_data(group, new_file)
				group = []
			else:
				group.append(line.strip())
		new_file = p2_create_group_data(group, new_file)
		return new_file

def p2_get_sum_of_counts(grouped_data):
	count = 0
	for group in grouped_data:
		count+=len(group)
	return count

def part_2():
    data = p2_create_data()
    count = p2_get_sum_of_counts(data)
    print(f'part 2: {count}')

part_1()
part_2()

