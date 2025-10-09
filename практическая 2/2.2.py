import sympy as sp
x1 = input("Введите выражение для x: ")
y1 = input("Введите выражение для y: ")
z1 = input("Введите выражение для z: ")
x = sp.sympify(x1)
y = sp.sympify(y1)
z = sp.sympify(z1)
n = (9 + (x - y)**2)**(1/3)
d = x**2 + y**2 + 2
t1 = n / d
t2 = sp.exp(abs(x - y))
t3 = sp.tan(z)**3
s = t1 - t2 * t3
s_value = s.evalf()
print(f"Результат: {float(s_value):.5f}")
