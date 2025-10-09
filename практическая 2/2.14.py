import sympy as sp
x1 = input("Введите выражение для x: ")
y1 = input("Введите выражение для y: ")
z1 = input("Введите выражение для z: ")
x = sp.sympify(x1)
y = sp.sympify(y1)
z = sp.sympify(z1)
p = y**(x + 1)
c = sp.cbrt(sp.Abs(y - 2))
f = p
f1 = c + 3
fr = f / f1
fn = x + y / 2
fd = 2 * sp.Abs(x + y)
fr1 = fn / fd
sin_part = sp.sin(z)
p2 = (x + 1)**(-1 / sin_part)
s = fr + fr1 * p2
s_value = s.evalf()
print(f"Результат: {s_value:.6g}")