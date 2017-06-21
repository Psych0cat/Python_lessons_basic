# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа

answer = ""
for char in str(number):
    if char > answer:
        answer = char
print (answer)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу используя только две переменные

i = input("Enter the first number>>")
j = input("Enter the second number>>")
i, j = j, i
print ("Now first is", i, "second is", j)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида ax2 + bx + c = 0.
# Для вычисления квадратного корня воспользуйтесь функицй sqrt() молудя math
# import math
# math.sqrt(4) - вычисляет корень числа 4

a = int(input('Enter "a"'))
b = int(input('Enter "b"'))
c = int(input('Enter "c"'))
import math
try:
    d = (b ** 2) - (4 * a * c)
    solution1 = (-b - math.sqrt(d)) / (2*a)
    solution2 = (-b + math.sqrt(d)) / (2*a)
    print (solution1)
    print (solution2)
except:
    print ("Invalid input or no solutions.")