def get_data():
	with open('data.in', 'r') as data_file:
		data = [line.strip().split('x') for line in data_file]
		return data


def part_1():
	data = get_data()
	total_paper = []
	for i in data:
		#print(i)
		l, w, h = [int(j) for j in i]
		#2*l*w + 2*w*h + 2*h*l
		wrapping_paper = (2*(l*w + w*h + h*l) + min([l*w, w*h, h*l]))
		total_paper.append(wrapping_paper)
	return sum(total_paper)
print(part_1())

def get_shortest_perimeter(l, w, h):
	dimensions = [l, w, h]
	shortest = min(dimensions)
	dimensions.remove(shortest)
	second_shortest = min(dimensions)
	perimeter = 2*(shortest + second_shortest)
	return perimeter

def get_volume(l, w, h):
	return l*w*h

def part_2():
	data = get_data()
	ribbon_lengths = []
	for i in data:
		l, w, h = [int(j) for j in i]
		perimeter = get_shortest_perimeter(l, w, h)
		volume = get_volume(l, w, h)
		length = volume + perimeter
		ribbon_lengths.append(length)
	return sum(ribbon_lengths)

print(part_2())
		
		
