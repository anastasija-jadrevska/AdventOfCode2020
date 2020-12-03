
int_list = []
with open('input1.txt') as f:
    for line in f:
        int_list.append(int(line))


def func(list, last):

    count = 1
    for i in list:
        if i != list[last]:
            for y in range(count, last):
                if (i + int_list[y]) < 2020:
                    for x in list:
                        if x == 2020 - (i + int_list[y]):
                            return i, int_list[y], x


def funcUpd(list):

    for i in list:
        for y in list:
            if 2020-i-y in list:
                return (2020 -i-y)*i*y


a, b , c= func(int_list, len(int_list) - 1)

print(a*b*c)
print(funcUpd(int_list))