n = (input('Введите шестизначное число: '))
print(['NO', 'YES'][sum(list(map(int, n[:3])))==sum(list(map(int, n[3:])))]) 