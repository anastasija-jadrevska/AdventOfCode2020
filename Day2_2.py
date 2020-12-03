passw = []
with open('input2.txt') as f:
    for line in f:
        passw.append(line)

count = 0
for i in passw:

    temp = i.split(": ")
    check = temp[0].split(" ")

    # -1 becasuse first index is 1
    place1 = int(check[0].split("-")[0])-1
    place2 = int(check[0].split("-")[1])-1

    password = list(temp[1])

    if check[1] == password[place1] and check[1] != password[place2] or \
            check[1] != password[place1] and check[1] == password[place2]:
        count += 1

print(count)
