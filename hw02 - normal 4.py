# Задача-4: Дан список, заполненный произвольными целыми числами
# Получите новый список, элементами которого будут только уникальные элементы исходного
# Например, lst = [1,2,4,5,6,2,5,2], нужно получить lst2 = [1,4,6]

import random
a = 0
lst = list()
while a < 20 :
  lst.append(random.randint(0,10))
  a += 1
print (lst)

print ('-'*50)

lst2 = list()
for i in lst :
  if i not in lst2 :
    lst2.append(i)
  else : continue
print (lst2)

print ('-'*50)

d = {}
lst3 = list()
for i in lst :
  d[i] = d.get(i, 0) + 1
#print (d)
for key, value in d.items() :
  if value == 1 :
    lst3.append(key)
print (lst3)