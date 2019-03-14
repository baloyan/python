# Задача-2:
# Даны два произвольные списка. Удалите из первого списка элементы, присутствующие во втором списке.

lst1 = [1, 3, 5, 7, 9]
lst2 = [3, 8, 6, 5]
res = []
print(lst1, lst2)
for i in lst1:
    if i not in lst2:
        res.append(i)
lst1 = res
print(lst1, lst2)
print()