import sympy as sp
x1 = input("Введите выражение для x: ")
y1 = input("Введите выражение для y: ")
z1 = input("Введите выражение для z: ")
x = sp.sympify(x1)
y = sp.sympify(y1)
z = sp.sympify(z1)
abs_diff = sp.Abs(x - y)
exp_part = sp.exp(abs_diff)
p = abs_diff**(x + y)
denominator = sp.atan(x) + sp.atan(z)
f = (exp_part * p) / denominator
c = sp.cbrt(x**6 + sp.ln(y)**2)
s = f + c
s_value = s.evalf()
print(f"Результат: {s_value:.6g}")