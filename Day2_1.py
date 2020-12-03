
passw = []
with open('input2.txt') as f:
    for line in f:
        passw.append(line)

count = 0
for i in passw:
    rang = []
    temp = i.split(": ")
    check = temp[0].split(" ")
    min = int(check[0].split("-")[0])
    max = int(check[0].split("-")[1])

    if min <= temp[1].count(check[1]) <= max:
        count += 1
        print("pass")

print(count)
