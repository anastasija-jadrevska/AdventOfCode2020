inp = []
with open('input3.txt') as f:
    for line in f:
        strip = list(line.strip())
        inp.append(strip)


def make_move(right, down):
    global inp
    global curr_pos
    global count
    global flying

    if inp[curr_pos[0]][curr_pos[1]] == "#":
        count += 1

    if len(inp[curr_pos[0]]) - curr_pos[1] > right:
        curr_pos[1] += right
    else:
        curr_pos[1] = right - (len(inp[curr_pos[0]]) - curr_pos[1])
    curr_pos[0]+=down
    if (curr_pos[0]) >= len(inp):
        flying = False


to_check = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
result = 1
for i in to_check:
    count = 0
    curr_pos = [0, 0]
    flying = True
    while flying:
        make_move(i[0], i[1])
    result *= count

print(result)
