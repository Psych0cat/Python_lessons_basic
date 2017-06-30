# Задание-1:
# Напишите функцию возвращающую ряд Фибоначчи с n-элемента до m-элемент
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    pass

# Задача-2:
# Напишите функцию сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную фукцию и метод sort()

def sort_to_max(origin_list):
    new_list = []
    while origin_list:
        minimum = origin_list[0]
        for x in origin_list:
            if x < minimum:
                minimum = x
        new_list.append(minimum)
        origin_list.remove(minimum)
    print (new_list)
		        
sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])


# Задача-3:
# Напишите собственную реализацию функции filter
# Разумеется, внутри нельзя использовать саму функцию filter

def filter_new(func, old_seq):
    new_seq = []
    for item in old_seq:
        new_seq.append(func(item))
    print (new_seq)


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма

def is_rect(coords):
    """input: sequence of coordinates
	   output: true/false"""
    if len(coords) != 4:
        return False
    tA, tB, tC, tD = sorted(coords)
    return tA[0] == tB[0] and tC[0] == tD[0] and tA[1] == tC[1] and tB[1] == tD[1]
