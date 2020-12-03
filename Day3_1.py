inp = []
with open('input3.txt') as f:
    for line in f:
        strip = list(line.strip())
        inp.append(strip)

# length is 31 last index is 30   31-28 = 3 (0) 31-29=2 (1) 31 -30 = 1 (2)
# depth is 323


step = 3
count = 0
curr_pos = 0

def make_move(stage):
    global curr_pos
    global count
    if stage[curr_pos] == "#":
        print("yes")
        count += 1
    if len(stage) - curr_pos > step:
        curr_pos+=3
    else:
        curr_pos = step- (len(stage) - curr_pos)

    print(stage)
    print(curr_pos)



for i in inp:

    make_move(i)
print(count)