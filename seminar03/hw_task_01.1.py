# Первая задача:
# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению


# Вариант 1

from random import randint

length = int(input("Please enter the length of the list: "))
x = int(input("Please enter the number we are looking for: "))

my_list = [randint(1,100) for i in range(length)]

print(my_list)

# count_dict = {}
# 
# for item in my_list:
#     count_dict[item] = count_dict.get(item,0) + 1

ans = 0

for item in my_list:
    if (item == x): ans += 1

step = 1
found = False

if ans>0:
    print(f"{x} repeats {ans} times")
else:
    while found == False:
        step_up = x+step
        step_down = x-step
        for item in my_list:
            if (step_up == item) or (step_down == item):
                found = True
                print(f"{x} is not in the list, but the nearest number is: {item}")   
                break
        step += 1
        
# но тут для каждого step надо пробегать весь список заново, поэтому см вариант 2
    