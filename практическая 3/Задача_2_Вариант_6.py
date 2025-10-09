a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
if a < b and b > 4:
    x = a + b
elif a > b:
    x = a - b
else:
    x = a ** 2
print(f"Значение x: {x}")