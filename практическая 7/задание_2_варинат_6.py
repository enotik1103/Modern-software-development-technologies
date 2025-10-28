import math
def h(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
a = float(input("Введите первую сторону a: "))
b = float(input("Введите вторую сторону b: "))
c = float(input("Введите третью сторону c: "))
d = float(input("Введите четвертую сторону d: "))
p = float(input("Введите длину диагонали p: "))
area1 = h(a, b, p)
area2 = h(c, d, p)
area3 = area2 + area2
print(f"Площадь четырехугольника: {area3:.2f}")