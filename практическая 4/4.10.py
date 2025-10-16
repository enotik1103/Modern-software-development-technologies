def fibonacci(K, N):
    prev, curr = 0, 1
    for _ in range(K - 1):
        prev, curr = curr, prev + curr
    result_sum = 0
    for _ in range(N):
        result_sum += prev
        prev, curr = curr, prev + curr
    return result_sum
K = int(input("Введите начальный индекс K: "))
N = int(input("Введите количество чисел N: "))
result = fibonacci(K, N)
print(f"Сумма {N} чисел Фибоначчи, начиная с индекса {K}: {result}")