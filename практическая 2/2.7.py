import sympy as sp
x1 = input("Введите выражение для x: ")
y1 = input("Введите выражение для y: ")
z1 = input("Введите выражение для z: ")
x = sp.sympify(x1)
y = sp.sympify(y1)
z = sp.sympify(z1)
arctg_x = sp.atan(x)
arccos_x = sp.acos(x)
abs_d = sp.Abs(x - y)
d = abs_d * z + x**2
n = (x + 3)*abs_d + x**2
f = n / d
s = 5 * arctg_x - (1/4) * arccos_x * f
s_value = s.evalf()
print(f"Результат: {s_value:.6g}")