from aocd.models import Puzzle
import numpy as np
from matplotlib import pyplot as plt

puzzle = Puzzle(year=2019, day=8)
data = [int(i) for i in puzzle.input_data]
shape = (int(len(data) / 6 / 25), 6, 25)

# build 3d array
arr = np.array(data).reshape(shape)

# part 1
min_zero = min(arr, key=lambda x: len(x[x == 0]))
ones = len(min_zero[min_zero == 1])
twos = len(min_zero[min_zero == 2])
print("the result of part one: {} * {} = {}".format(ones, twos, ones * twos))

# part 2
def find_value(n):
    index = 0
    while n[index] == 2: index += 1
    return n[index]

message = np.apply_along_axis(find_value, 0, arr)
plt.imshow(message)
plt.show()
