# Задача-1:
# Дан список заполненный произвольными целыми числами, получите новый список элементами которого будут
# квадратные корни элементов исходного списка, но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math
nams = [2, -5, 8, 9, -25, 25, 4]
#генерируем квадраты положительных чисел, int которых равен float
print ([int(math.sqrt(num))for num in nums if num > 0 and int(math.sqrt(num)) == float(math.sqrt(num))])

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

date = input("Enter date >> ")
date = date.split(".")
days = {"01":"первое","02":"второе", "03":"третье"}
months = {"01":"декабря", "02": "января", "03": "февраля"}
print (days[date[0]], months[date[1]], date[2], "года")

# Задача-3: Напишите алгоритм заполняющий список произвольными целыми числами в диапазоне от -100 до 100
# В списке должно быть n - элементов
# Подсказка: для получения случайного числа изпользуйте функцию randint() модуля random

import random
n = int(input("Enter positive number >> "))
print ([random.randint(-100, 100) for num in range(n)])


# Задача-4: Дан список заполненный произвольными целыми числами
# Получите новый список, элементами которого будут только уникальные элементы исходного

print ([num for num in set(my_list)])
