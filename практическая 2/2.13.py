import sympy as sp
x1 = input("Введите выражение для x: ")
y1 = input("Введите выражение для y: ")
z1 = input("Введите выражение для z: ")
x = sp.sympify(x1)
y = sp.sympify(y1)
z = sp.sympify(z1)
c = sp.cbrt(x - 1)
n = sp.root(y + c, 4)
sin_p = sp.sin(z)**2
tg_part = sp.tan(z)
d = sp.Abs(x - y) * (sin_p + tg_part)
s = n / d
s_value = s.evalf()
print(f"Результат: {s_value:.6g}")