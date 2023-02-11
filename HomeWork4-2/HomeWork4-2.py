import random
N = int(input('Введите количество кустов на грядке: '))
massive1 = [random.randint(1, 10) for i in range(N)]
print(massive1)
maximum = 0
i = 0
total = 0
for i in range(i, N-2):
    total = massive1[i] + massive1[i+1] + massive1[i+2]
    if total > maximum:
        maximum = total
    i += 1
if massive1[0] + massive1[-1] + massive1[-2] > maximum:
    maximum = massive1[0] + massive1[-1] + massive1[-2]
if massive1[0] + massive1[1] + massive1[-1] > maximum:
    maximum = massive1[0] + massive1[1] + massive1[-1]
print(f'Наибольшее количество ягод  {maximum}') 
