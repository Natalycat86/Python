import random
N = int(input('Введите количество элементов в массиве: '))
massive = [random.randint(1, 9) for i in range(N)]
print(massive)
number = len(massive) - 1
X = massive[number]
print(f"Последний элемент массива = {X}")
result = massive.count(X)
print(f"Число {X} встречается в массиве {result} раз") 