def factorial_sum(n):
    fact = 1
    total_sum = 0
    for i in range(1, n + 1):
        fact *= i
        total_sum += fact
    return total_sum
n = int(input("Введите натуральное число n: "))
result = factorial_sum(n)
print(result)