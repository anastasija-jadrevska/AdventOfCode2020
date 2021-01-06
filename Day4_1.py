
int_list = []
with open('input4.txt') as f:
    for line in f:

        int_list.append(line.strip())

temp = []
main = []
for i in int_list:
    if i == '':
        print(temp)
        main.append(temp)
        temp = []
    else:
        temp_val = i.split(" ")
        for j in temp_val:
            j = j.split(":")[0]
            temp.append(j)
    if i == int_list[len(int_list)-1]:
        print(temp)
        main.append(temp)

check = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

count = 0
for m in main:
    temp_c = 0
    for c in check:
        if c in m:
            temp_c+=1
    if temp_c == len(check):
        count+=1




print(count)


