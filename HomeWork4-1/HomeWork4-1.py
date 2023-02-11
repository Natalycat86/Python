import random
M = int(input('Введите количество элементов в первом множестве: '))
N = int(input('Введите количество элементов во втором множестве: '))
massive1 = [random.randint(1, 20) for i in range(N)]
massive2 = [random.randint(1, 20) for i in range(M)]
print(massive1)
print(massive2)
my_set1 = set(massive1)
my_set2 = set(massive2)
my_set3 = (my_set1.intersection(my_set2))
print(sorted(my_set3)) 
 