import math
def rec(n, divisor=2):
    if n <= 1:
        return False
    elif divisor * divisor > n:
        return True
    elif n % divisor == 0:
        return False
    else:
        return rec(n, divisor + 1)
def num():
    n = int(input("Введите натуральное число n > 1: "))
    if rec(n):
        print("YES")
    else:
        print("NO")
num()