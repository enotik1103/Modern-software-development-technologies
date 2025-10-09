import sympy as sp
x1 = input("Введите выражение для x: ")
y1 = input("Введите выражение для y: ")
z1 = input("Введите выражение для z: ")
x = sp.sympify(x1)
y = sp.sympify(y1)
z = sp.sympify(z1)
p = x**(y/x)
c = sp.cbrt(y/x)
exp_part = sp.exp(x - 1/sp.sin(z))
c = sp.cbrt(exp_part)
f = sp.root(sp.Abs(y), 4)
sqrt_p = sp.sqrt(x + f) * c
s = 2**(-x) * sqrt_p
s_value = s.evalf()
print(f"Результат: {s_value:.6g}")