#day 10 .py
import itertools
def get_data():
	with open ('test2.in', 'r') as data_file:
		data = [int(i) for i in data_file]
	return data
def part_1():
	data = get_data()
	data.append(0)#the plug
	data.append((max(data))+3)#the device
	sorted_data = sorted(data)
	differences = [sorted_data[i+1]-sorted_data[i] for i in range(len(sorted_data)-1)]
	one_j_differences = len([i for i in differences if i == 1])
	three_j_differences = len([i for i in differences if i == 3])
	return one_j_differences * three_j_differences

print(part_1())
#561 too low

def part_2():
	correct_arrangements = []
	data = get_data()
	device = max(data)+3
	sorted_data = sorted(data)
	for j in range(len(sorted_data)):
		permutations = itertools.combinations(sorted_data, j)
		for perm in permutations:
			p = [i for i in perm]
			p.append(0)
			p.append(device)
			sorted_p = sorted(p)
			differences = [sorted_p[i+1]-sorted_p[i] for i in range(len(sorted_p)-1)]
			valid = True
			for diff in differences:
				if diff > 3:
					valid = False
			if valid == True and sorted_p not in correct_arrangements:
				correct_arrangements.append(sorted_p)
	print(correct_arrangements)
	print(len(correct_arrangements))
 
part_2()	
