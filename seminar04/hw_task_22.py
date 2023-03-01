# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint

l = int(input("Please set the length of the first list: "))
m = int(input("Please set the length of the second list: "))

list_1 = []
list_2 = []

while len(list_1) != l:
    list_1 = input("Please enter the elements of list one (divided by space): ").split()
while len(list_2) != m:
    list_2 = input("Please enter the elements of list two (divided by space): ").split()

list_3 = list_1 + list_2

list_3 = list(set(list_3))

for i in range(len(list_3)):
    min = list_3[i]
    min_ind = i
    for j in range(i,len(list_3)):
        if list_3[j]<min:
            min = list_3[j]
            min_ind = j
    tmp = list_3[i]
    list_3[i] = list_3[min_ind]
    list_3[min_ind] = tmp
    
print(list_3)