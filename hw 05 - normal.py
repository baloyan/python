# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import sys
import shutil


def my_mkdir(my_dir):
    try:
        os.mkdir(my_dir)
        print ('Папка создана')
    except FileExistsError:
        print ('Папка уже существует')


def my_deldir(my_dir):
    try:
        os.rmdir(my_dir)
        print ('Папка удалена')
    except FileNotFoundError:
        print ('Папка не существует')


def my_listdir():
    try:
        print ('\nСписок директорий, без файлов в текущем каталоге:\n')
        list_dir = os.listdir(".")
        return list_dir
    except Exception as e:
        print (e)


def my_chdir(my_dir):
    try:
        os.chdir(my_dir)
        print ('Вы перешли в папку: {}'.format(my_dir))
    except FileNotFoundError:
        print ('Папка не существует')

print ('''Выберите действие:
1. Перейти в папку
2. Просмотреть содержимое текущей папки
3. Удалить папку
4. Создать папку
5. Выйти
''')

task = int(input('Введите число от 1 от 5:'))
while task != 5:
    if task == 4:
        dir_name =  str(input('Введите названиет папки, для создания:'))
        my_mkdir(dir_name)
    elif task == 3:
        dir_name =  str(input('Введите названиет папки, для удаления:'))
        my_deldir(dir_name)
    elif task == 2:
        print(my_listdir())
    elif task == 1:
    	dir_name =  str(input('Введите названиет папки, для перехода:'))
    	my_chdir(dir_name)
    task = int(input('Введите число от 1 от 5:'))