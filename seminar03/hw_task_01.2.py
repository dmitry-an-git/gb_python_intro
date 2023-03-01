# Первая задача:
# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению


# Вариант 2

from random import randint

length = int(input("Please enter the length of the list: "))
x = int(input("Please enter the number we are looking for: "))
max_rand = 100

my_list = [randint(1,max_rand) for i in range(length)]
my_index = [0 for i in range(max_rand+1)]

print(my_list)

for item in my_list:
    my_index[item] += 1 # список где на каждом индексе счетчик соответствующего значения в основном списке
    
print(my_index)

found = False
    
if my_index[x] > 0:
    print(f"{x} repeats {my_index[x]} times")
else:
    for step in range(1,max_rand+1):

        step_down = max(0,x-step) # чтобы не выйти за пределы списка
        step_up = min(length+1, x+step) # чтобы не выйти за пределы списка

        if my_index[step_down]>0:
            nearest = step_down
            found = True
        elif my_index[step_up]>0:
            nearest = step_up
            found = True

        if found == True:
            print(f"{x} is not in the list, but the nearest number is: {nearest}")   
            break
