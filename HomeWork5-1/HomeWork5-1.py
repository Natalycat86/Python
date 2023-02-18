def exponentiation(A,B):
    if (B == 1):
        return (A)
    elif (B != 1):
        return (A * exponentiation(A, B - 1))
    
    
A = int(input("Введите число: "))
B = int(input("Введите степень числа: "))
print("Результат возведения в степень равен:", exponentiation(A, B))
