def fibonacci_sum(N):
    if N <= 0:
        return 0
    a, b = 0, 1   
    sum_fib = 0   
    for _ in range(N):
        sum_fib += a       
        a, b = b, a + b    
    return sum_fib
N = int(input("Введите число N: "))
result = fibonacci_sum(N)
print(f"Сумма первых {N} чисел Фибоначчи: {result}")