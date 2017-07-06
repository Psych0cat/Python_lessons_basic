# Задача-1:
# Напишите скрипт создающий директории dir_1 - dir_9 в папке из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

def folder_creator(n):
    for i in range(1, n + 1):
        os.mkdir("dir_{0}".format(i))

def folder_deleter(n):
    for i in range(1, n + 1):
        os.rmdir("dir_{0}".format(i))


# Задача-2:
# Напишите скрипт отображающий папки текущей директории

import os

def get_cwd():
    print (os.getcwd())

# Задача-3:
# Напишите скрипт создающий копию файла, из которого запущен данный скрипт

import os

import shutil
shutil.copy2(os.path.abspath(__file__), os.path.dirname(os.path.abspath(__file__)) + "\copy.py")