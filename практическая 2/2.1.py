import sympy as sp
x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))
z = input("Введите значение z: ")
z = sp.sympify(z)
z_value = z.evalf()
s = (2 * sp.cos(x - 2/3)) / (1/2 + sp.sin(y)**2) * (1 + z_value**2 / (3 - z_value**2 / 5))
print(f"Результат: {s.evalf():.2f}")