import sympy as sp
x1 = input("Введите выражение для x: ")
y1 = input("Введите выражение для y: ")
z1 = input("Введите выражение для z: ")
x = sp.sympify(x1)
y = sp.sympify(y1)
z = sp.sympify(z1)
sx = sp.sqrt(sp.Abs(x))
yp = y**(-sx)
lnp = sp.ln(sp.Abs(yp))
b = x - y / 2
arctg_z = sp.atan(z)
sinp = sp.sin(arctg_z)**2
s = lnp * b + sinp
s_value = s.evalf()
print(f"Результат: {float(s_value):.5f}")