import pprint
with open('test.in', 'r') as data_file:
	data = [line.strip() for line in data_file]
	#print(data)



#ll mned to secify for edge seats beacause they dont hav eones to left / right
#while list != previous list
print(len(data))
#runs for each seat to get te adjacebt ones
def get_adjacent_seats(seats, row, seat):
	adjacent_seats = []
	for i in range(-1, 2):
		for j in range(-1, 2):
			#print(i, j)
			try:
				ri = row + i
				si = seat + j
				if (0 <= ri <= 91 and 0<=si<=94) and not(ri==0 and si==0): 
					adjacent_seats.append(seats[ri][si])
			except IndexError:
				pass
	return adjacent_seats



seats = data
#returns all adjacent seats
adjacent_seats = []
for row_no, row in enumerate(seats):
	adjacent_seats_per_row = []
	for seat_no, seat in enumerate(row):
		adjacent_seats_per_row.append(get_adjacent_seats(seats, row_no, seat_no))
	adjacent_seats.append(adjacent_seats_per_row)
print(len(adjacent_seats))
previous_seats = seats
all_arrangements = []
seats_after_round = []
all_arrangements.append(['TEMP'])
all_arrangements.append(seats)
count = 0
while count == 0 or (all_arrangements[count] != all_arrangements[count-1]):
	#round one
	seats_after_round = []
	for row_no, row in enumerate(seats):
		row_after_round = []
		for seat_no, seat in enumerate(row):
			if seat == 'L' and adjacent_seats[row_no][seat_no].count('#') == 0:
				row_after_round.append('#')
			elif seat == '#' and adjacent_seats[row_no][seat_no].count('#')>=4:
				row_after_round.append('L')
			else:
				row_after_round.append(seat)
		seats_after_round.append(row_after_round)
	all_arrangements.append(seats_after_round)
	count += 1
	print(count)
for row in seats_after_round:
	print(row)
#count how many # in seats after round
counts = [row.count('#') for row in seats_after_round]
print(sum(counts))
