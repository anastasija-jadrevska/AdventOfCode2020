import math
inp = []
with open('input5.txt') as f:
    for line in f:
        strip = list(line.strip())
        inp.append(strip)

rows = []
seats = []
for i in range(0, 127):
    rows.append(i)
for j in range(0, 7):
    seats.append(j)


def find_row(code):
    L = 0
    R = len(rows)
    for p in range (0, 7):
        m = (R+L)/2
        if code[p] == "F":
            R = math.floor(m)
        else:
            L = math.ceil(m)
    return L


def find_seat(code):
    L = 0
    R = len(seats)
    for p in range (7, 10):
        m = (R+L)/2
        if code[p] == "L":
            R = math.floor(m)
        else:
            L = math.ceil(m)
    return L



temp = 0
ids = []

for k in inp:
    id = (find_row(k) * 8) + find_seat(k)
    ids.append(id)
    if id > temp:
        temp = id

print("Highest id is {}".format(temp))

# Part 2
ids.sort()
print("Result is {}".format(next(x for x in range(ids[0], ids[-1] + 1) if x not in ids)))


