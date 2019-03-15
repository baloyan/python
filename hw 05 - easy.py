import os
import sys
import shutil
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
print ('Задание 1:\n')
def my_mkdir():
    i = 1
    while i < 10:
        try:
            os.mkdir("dir_{}".format(i))
            print ('Папка создана')
        except FileExistsError:
            print ('Папка уже существует')
        i+=1

def my_deldir():
    i = 1
    while i < 10:
        try:
            os.rmdir("dir_{}".format(i))
            print ('Папка удалена')
        except FileNotFoundError:
            print ('Папка не существует')
        i+=1

my_mkdir()
my_deldir()


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
print ('Задание 2:\n')
def my_listdir():
    try:
        print ('\nСписок директорий, без файлов в текущем каталоге:\n')
        list_dir = os.listdir(".")
        for dir_ in list_dir:
            is_dir = os.path.isdir(dir_)
            if is_dir:
                print (dir_)
    except Exception as e:
        print (e)

my_listdir()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого
# запущен данный скрипт.

print ('Задание 3:\n')
try:
    shutil.copy(sys.argv[0], 'copy-{}'.format(sys.argv[0]))
except IOError:
    print ('Ошибка создания копии')

print (os.listdir("."))