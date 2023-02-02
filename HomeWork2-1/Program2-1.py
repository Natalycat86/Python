i = 0
b = 0
count = 0
A = int(input('Введите количество монет: '))
from random import randint
list = [randint(0, 1) for i in range (A)]
print(list)
while (b < A):
    if 0 in list:
        count += 1
        b += 1
print (count)