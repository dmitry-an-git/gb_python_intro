# Задача 26: Напишите программу, которая на вход принимает два числа A и B, 
#     и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3^5) 
# A = 2; B = 3 -> 8

a = int(input("Please enter the first number (a): "))
b = int(input("Please enter the second number (b): "))

def power(c,d):
    if d == 0: return 1
    else: return c*power(c,d-1)
    
print(f"a^b equals {power(a,b)}")