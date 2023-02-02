a = int(input('Введите длину шоколадки: '))
b = int(input('Введите ширину шоколадки: '))
c = int(input('Сколько долек нужно: '))
if c < a * b and ((c % a == 0) or (c % b == 0)):
    print ('YES')
else:
    print ('No') 