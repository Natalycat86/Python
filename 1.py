a = int(input('введите число '))
i = 1
result = 1
while i <= a:
    if a == 0:
        result = 1
    else:
        result = result * i
        i = i + 1
    
print(result)