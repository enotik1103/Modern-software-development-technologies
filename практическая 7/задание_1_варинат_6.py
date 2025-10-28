def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
if __name__ == "__main__":
    A = int(input("Введите первое натуральное число: "))
    B = int(input("Введите второе натуральное число: "))
    nod = gcd(A, B)
    nok = (A * B) // nod
    print(f"НОД({A}, {B}) = {nod}")
    print(f"НОК({A}, {B}) = {nok}")