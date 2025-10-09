def sum_cubes(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 3
    return total
n = int(input("Введите число n: "))
result = sum_cubes(n)
print(f"Сумма кубов чисел от 1 до {n}: {result}")