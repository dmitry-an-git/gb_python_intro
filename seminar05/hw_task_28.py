# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
#     Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#    2 2 4

a = int(input("Please enter the first number: "))
b = int(input("Please enter the second number: "))

def summ(c,d):
    if d == 0: return c
    else: return summ(c+1,d-1)

print(f"Their sum is {summ(a,b)}")