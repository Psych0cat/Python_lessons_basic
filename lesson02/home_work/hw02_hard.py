# Задание-1: уравнение прямой вида y = kx - b задано ввиде строки.
# Определить координату y, точки с заданной координатой x

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y

equation = 'y = -12x + 11111140.2121'
x = 2.5
eq_list = (equation.split())
print (int(eq_list[2][:-1]) * x + float(eq_list[4]))

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy', проверить корректно ли введена дата
# Условия коррекности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31) (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год приводиться к целому положитеьному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом (т.е. 2 - для дня, 2- месяц, 4 -год)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'

def check_date(date):
    if len(date) != 10:
        print ("incorrect date format")
        return
    date = date.split('.')
    if int(date[0]) <0 or int(date[1]) <0 or int(date[2]) <0:
        print ("incorrect date format")
        return
    elif int(date[2]) not in range(1, 100000):
        print ("incorrect date format")
        return
    elif int(date[1]) not in range(1, 13):
        print ("incorrect date format")
        return
    elif int(date[1]) in [1, 3, 5, 7, 9, 11] and int(date[0]) not in range(1, 32):
        print ("incorrect date format")
        return
    elif int(date[1]) in [2, 4, 6, 8, 10, 12] and int(date[0]) not in range(1, 31):
        print ("incorrect date format")
        return
    else:
        print ("Date is correct!")
        return

# Задание-3: "Перевернутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню — расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната, затем идет два этажа
# на каждом из которых по две комнаты, затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача: нужно научится по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3
