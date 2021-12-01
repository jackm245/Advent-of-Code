import sys


w, h = 25, 6
with open(sys.argv[1], "r") as f:
    pixels = f.read().strip()

layers = [pixels[i : i + w * h] for i in range(0, len(pixels), w * h)]

fewest_0 = min(layers, key=lambda x: x.count("0"))
print(f"Part 1: {fewest_0.count('1')*fewest_0.count('2')}")

print(f"Part 2:")
for y in range(h):
    line = ""
    for x in range(w):
        l = 0
        while layers[l][x + (y * w)] == "2":
            l += 1
        line += layers[l][x + (y * w)]
    print(line.replace("1", chr(9608)).replace("0", " "))
