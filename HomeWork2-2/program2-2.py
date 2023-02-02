S = int(input('Введите сумму: '))
P = int(input('Введите произведение: '))
a = 1
b = 1
for a in range(1, 1001):
    for b in range(1, 1001):
        if (a + b == S and a*b == P):
            print (a, b) 