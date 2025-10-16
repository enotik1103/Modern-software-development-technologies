arr = []
for i in range(10):
    num = int(input(f"Введите {i+1}-е число: "))
    arr.append(num)
s = sum(x for x in arr if x > 5)
print("Сумма чисел, которые больше 5:", s)