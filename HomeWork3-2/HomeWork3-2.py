import random
N = int(input('Введите количество элементов в массиве: '))
massive = [random.randint(1, 50) for i in range(N)]
print(massive)
X = int(input('Введите число для поиска ближайшего к нему в массиве: '))
found = massive[0]
for item in massive:
    if abs(item - X) < abs(found - X):
        found = item
print(f'Ближайшее число к {X} в списке является {found}') 