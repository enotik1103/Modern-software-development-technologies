import sympy as sp
x1 = input("Введите выражение для x: ")
y1 = input("Введите выражение для y: ")
z1 = input("Введите выражение для z: ")
x = sp.sympify(x1)
y = sp.sympify(y1)
z = sp.sympify(z1)
c = x**(1/3)
x_p = x**(y + 2)
b = c+ x_p
sqrt_p = sp.sqrt(10 * b)
arcz = sp.asin(z)**2
abs_diff = sp.Abs(x - y)
s = sqrt_p * (arcz - abs_diff)
s_value = s.evalf()
print(f"Результат: {s_value:.6g}")