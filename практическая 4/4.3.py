A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
if A <= B:
    print("Ошибка: A должно быть больше B")
else:
    for i in range(A, B - 1, -1):
        if i % 2 != 0:
            print(i)