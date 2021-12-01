import sys
def get_data():
	with open('9.in', 'r') as data_file:
		data = [int(i) for i in data_file]
	return data

def part_1():
	preamble_length = 25
	data = get_data()
	for index, number in enumerate(data[:-preamble_length]):
		#print(index, number)
		preamble = data[index:index+preamble_length]
		value_to_check = data[index+preamble_length]
		#print(preamble, value_to_check)
		valid = False
		for number_1 in preamble:
			for number_2 in preamble:
				if number_1 + number_2 == value_to_check:
					valid = True
		if valid == False:
			return value_to_check


def part_2():
	invalid_number = part_1()
	data = get_data()
	contiguous_numbers = []
	for index, number in enumerate(data):
		contiguous_numbers.append(number)
		count = 1
		while 1:
			if sum(contiguous_numbers) < invalid_number:
				contiguous_numbers.append(data[index+count])
				count += 1
			elif sum(contiguous_numbers) == invalid_number:
					#print(contiguous_numbers)
					result = min(contiguous_numbers) + max(contiguous_numbers)
					return result
			else:
				contiguous_numbers = []
				break
		#print(index)


def main():
	print(f'part 1: {part_1()}')
	print(f'part 2: {part_2()}')

if __name__ == '__main__':
	main()
