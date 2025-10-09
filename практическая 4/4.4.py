N = int(input("Введите количество чисел N: "))
sum_num = 0
for _ in range(N):
    num = int(input("Введите число: "))
    sum_num += num
print("Сумма чисел:", sum_num)