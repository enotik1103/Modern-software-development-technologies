import sympy as sp
x1 = input("Введите выражение для x: ")
y1 = input("Введите выражение для y: ")
z1 = input("Введите выражение для z: ")
x = sp.sympify(x1)
y = sp.sympify(y1)
z = sp.sympify(z1)
p = x**(y + 1)
exp_part = sp.exp(y - 1)
tg_part = sp.tan(z)
f = 1 + x * sp.Abs(y - tg_part)
fr1 = (p + exp_part) / f
abs_diff = sp.Abs(y - x)
fr2 = abs_diff**2 / 2
fr3 = abs_diff**3 / 3
fr4 = 1 + abs ( y-x )
s = fr1 * fr4 + fr2 - fr3
s_value = s.evalf()
print(f"Результат: {s_value:.6g}")