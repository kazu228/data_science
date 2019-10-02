import random

number_list = list(range(1, 11))
random.shuffle(number_list)
print(number_list)


result_list = []
for y in range(1, 11):
    min = 11
    for x in number_list:  # 最小値を得る
        if min > x:
            min = x

    result_list.append(min)
    number_list.remove(min)

print(result_list)