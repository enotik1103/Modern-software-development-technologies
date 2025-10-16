n = int(input("Введите натуральное число n: "))
if n < 0:
    print("Факториал отрицательного числа не определен.")
elif n == 0 or n == 1:
    print(f"{n}! = 1")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"{n}! = {factorial}")