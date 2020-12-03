
int_list = []
with open('input1.txt') as f:
    for line in f:
        int_list.append(int(line))


def func(list, last):

    count = 1
    for i in list:
        if i != list[last]:
            for y in range(count, last):
                if i + int_list[y] == 2020:
                    return i, int_list[y]


def funcUpdate(list):
    for i in list:
        if 2020-i in list:
            return i * ( 2020-i)


a, b = func(int_list, len(int_list) - 1)

print(a*b)
print(funcUpdate(int_list))