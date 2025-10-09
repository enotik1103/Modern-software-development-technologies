import sympy as sp
x1 = input("Введите выражение для x: ")
y1 = input("Введите выражение для y: ")
z1 = input("Введите выражение для z: ")
x = sp.sympify(x1)
y = sp.sympify(y1)
z = sp.sympify(z1)
n = (1 + 2 * sp.sin(y)**2)
d = abs(sp.cos(x) - sp.cos(y))
t1 = d**n
t2 = (1 + z + z**2 / 2 + z**3 / 3 + z**4 / 4)
s = t1 * t2
s_value = s.evalf()
print(f"Результат: {float(s_value):.5f}")