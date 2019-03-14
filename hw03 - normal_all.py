# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Есть условие, не отображать людей получающих более зарплату 500000
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату - 13% (налоги ведь),
# где имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.

import os
import math
names = ['Vasya', 'Anton', 'Oleg', 'Sergey', 'Alexandr', 'Andrey']
salary = [10000, 15000, 710000, 18000, 13500, 1000000]

PATH = r'C:\Users\Lenovo\Documents\GitHub\GeekBrains'
FILE_NAME = 'salary.txt'

full_path = os.path.join(PATH, FILE_NAME)

my_list = dict (zip (names,salary))

with open(full_path, 'w', encoding='UTF-8') as file:
        for key, item in my_list.items():
            if item < 500000:
                 file.write('{} - {}\n'.format(key, item))
file.close()
my_new_list = []
with open(full_path, 'r', encoding='UTF-8') as file:
    for f in file.readlines():
        my_new_list.append(f.splitlines())

    for el in my_new_list:
        el = ''.join(el)
        print(el)
        x = int (el.split(' ')[2])
        x = str (math.trunc(x - (x * 0.13)))
        del (el.split(' ')[2])
        print(el)
        el.split(' ')[2] = x
        print(el)

print(my_new_list)