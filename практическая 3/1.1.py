num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))
result = []
if 1 <= num1 <= 3:
    result.append(num1)
if 1 <= num2 <= 3:
    result.append(num2)
if 1 <= num3 <= 3:
    result.append(num3)
if result:
    print("Числа, принадлежащие интервалу [1, 3]:", result)
else:
    print("Числа, принадлежащих интервалу, не найдены [1, 3].")