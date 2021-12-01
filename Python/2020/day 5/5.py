def binary_to_dinary(binary):
	return int(binary, 2)

def convert_to_binary(chars):
	binary_value = []
	for char in chars:
		if char == "F" or char == "L":
			binary_value.append('0')
		else:
			binary_value.append('1')
	return ''.join(binary_value)

def get_seat_id(row, column):
	return int(row)*8 + int(column)

def get_muiltiplied_value(boarding_pass):
	row = boarding_pass[:7]
	column = boarding_pass[-3:]
	#print(row, column)
	row_binary = convert_to_binary(row)
	column_binary = convert_to_binary(column)
	row_number = binary_to_dinary(row_binary)
	column_number = binary_to_dinary(column_binary)
	#print(row_number, column_number)
	return get_seat_id(row_number, column_number)

def get_all_seat_ids():
	with open('5.in', 'r') as data_file:
		data = [line.strip() for line in data_file]
		#print(data)
	seat_id_list = [get_muiltiplied_value(boarding_pass) for boarding_pass in data]
	return seat_id_list

def get_free_seat():
	seat_id_list = get_all_seat_ids()
	#print(seat_id_list)
	max_seat = max(seat_id_list)
	print(f'The highest seat number is: {max_seat}')
	all_possible_seats = [i for i in range(0, max_seat + 1)]
	for seat in seat_id_list:
		#print(seat)
		all_possible_seats.remove(int(seat))
	desired_seat = int(''.join([str(i) for i in all_possible_seats if(i+1 not in all_possible_seats) and (i-1 not in all_possible_seats)]))
	print(f'My seat is number: {desired_seat}')

get_free_seat()
