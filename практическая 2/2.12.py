import sympy as sp
x1 = input("Введите выражение для x: ")
y1 = input("Введите выражение для y: ")
z1 = input("Введите выражение для z: ")
x = sp.sympify(x1)
y = sp.sympify(y1)
z = sp.sympify(z1)
c = sp.cbrt(sp.Abs(x))
p = y**x
exp_p = 2**p
p2 = (3**x)**y
arctg_part = sp.atan(z)
n = y * (arctg_part - 1/3)
d = sp.Abs(x) + 1 / (y**2 + 1)
f = n / d
s = exp_p + p2 - f
s_value = s.evalf()
print(f"Результат: {s_value:.6g}")