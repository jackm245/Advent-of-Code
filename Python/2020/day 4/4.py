import re
from time import time
#looks to see if the value of each field is valid
def check_key(key, value):
	reg_ex = {
		'byr': '^((19[2-9]\d?)|20{2}[0-2])$',
		'iyr': '^(20((1\d)|20))$',
		'eyr': '^(20((2\d)|30))$',
		'hgt': '(^1(([5-8]\d)|(9[0-3]))cm$)|((^((59)|(6\d)|(7[0-6]))in$))',
		'hcl': '^#(\d|[a-f]){6}$',
		'ecl': '^(amb|blu|brn|gry|grn|hzl|oth)$',
		'pid': '^\d{9}$'
	}
	try:
		if re.search(reg_ex[key], str(value)) != None:
			return True
		return False
	except KeyError:
		return True


#creates the original file as a set of lists
#formats the data in a desired fashion
def create_data():
	with open('4.in') as raw_file:
		new_file = []
		accumulator = []
		for line in raw_file:
			if line != '\n':
				accumulator.append(line.strip().split())
			if line == '\n':
				new_file.append(accumulator)
				accumulator = []
		new_file.append(accumulator)
		return new_file

#returns a list of the lines that have all data present
def get_data_with_all_present_keys():
	new_file = create_data()
	#searches each data set to see if it has the required fields
	allowed_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
	validated = []
	for line in new_file:
		#print(line)
		flat_line = [item for sublist in line for item in sublist]
		sub_total = 0
		for term in flat_line:
			if term[:3] in allowed_keys:
				sub_total+=1
		#print(sub_total)
		if sub_total == 7:
			#print("valid")
			validated.append(flat_line)
			sub_total = 0
	print(len(validated))
	return validated

def main():
	start = time()
	#returns the line which have the correct number of fields and valid data in each field
	data = get_data_with_all_present_keys()
	#print(data)
	#print(len(data))
	valid_lines=[]
	for line in data:
		#print(len(line))
		valid = 0
		for term in line:
			#print(term)
			key = term[:3]
			value = term[4:]
			#print(key, value)
			if check_key(key, value):
				valid += 1
				#print("valid")
		#print("\n")
		if valid == len(line):
			valid_lines.append(line)
	print(len(valid_lines))
		#print(total)
	end = time()
	print(end-start)
main()
