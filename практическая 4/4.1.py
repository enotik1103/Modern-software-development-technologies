A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
if A > B:
    print("Ошибка: A должно быть меньше или равно B")
else:
    for i in range(A, B + 1):
        print(i)