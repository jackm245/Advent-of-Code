import sys
from time import sleep

def get_data(file_name):
	with open(file_name, 'r') as data_file:
		data = [(i[:i.strip().index(' ')].strip(), i[i.strip().index(' '):].strip())  for i in data_file]
	return data

def part_1():
	acc = 0
	i= 0
	data = get_data('8.in')
	lines_tried = []
	while 1:
		if i in lines_tried:
			return acc
		lines_tried.append(i)
		command, value = data[i]
		if command == 'acc':
			acc += int(value)
			i+=1
		elif command == 'jmp':
			i += int(value)
		else:
			i+=1



#runs the program with a given data set
def run_program(data, i=0, acc=0):
	try:
		#print(i, acc)
		command, value = data[i]
		#print(command, value)
		if command == 'acc':
			acc += int(value)
			i+=1
		elif command == 'jmp':
			i += int(value)
		else:
			i+=1
	except IndexError:
		return acc #terminates when the end of the file is reached
	except RecursionError:
		return False
	else:
		return run_program(data, i, acc)

#go through the list and for each jmp instruction change to nop and test the program
def part_2():
	for index, (command, value) in enumerate(get_data('8.in')):
		trial_data = get_data('8.in')
		if command == 'jmp':
			trial_data[index] = ('nop', value)
			result = run_program(trial_data)
			if int(result) != 0:
				return result

def main():
	print(f'part 1: {part_1()}')
	print(f'part 2: {part_2()}')

if __name__ == '__main__':
	main()
