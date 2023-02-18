def summa(A,B):
    if (B == 0):
        return (A)
    elif (B != 0):
        return summa (A + 1, B - 1)
    
    
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
print("Результат сложения чисел:", summa(A, B))