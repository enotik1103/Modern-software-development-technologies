import sympy as sp
x1 = input("Введите выражение для x: ")
y1 = input("Введите выражение для y: ")
z1 = input("Введите выражение для z: ")
x = sp.sympify(x1)
y = sp.sympify(y1)
z = sp.sympify(z1)
c = sp.cbrt(sp.Abs(x))
p = y**c
cos_p = sp.cos(y)**3
abs_d = sp.Abs(x - y)
sin_p = sp.sin(z)**2
sqrt_p = sp.sqrt(x + y)
n = abs_d * (1 + sin_p / sqrt_p)
d = sp.exp(abs_d) + x / 2
f = n / d
s = p + cos_p * f
s_value = s.evalf()
print(f"Результат: {s_value:.6g}")