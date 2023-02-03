i = 0
b = 0
count = 0
A = int(input('Введите количество монет: '))
from random import randint
list = [randint(0, 1) for i in range (A)]
print(list)
reshka = list.count(1)
orel = list.count(0)
if reshka > orel:
    print (orel)
else: print (reshka)  
