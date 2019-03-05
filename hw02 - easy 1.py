# Задача-1:
# Дан список фруктов. Напишите программу, выводящую фрукты в виде нумерованного списка, выровненного по правой стороне
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: использует метод .format()

lst = ["Яблоко", "Банан", "Киви", "Арбуз"]
maxlen = 0
for i in lst:
    if len(i) > maxlen:
        maxlen = len(i)
for i in range(len(lst)):
    print(("{0}. {1:>" + str(maxlen) + "}").format(i + 1, lst[i]))
print()

