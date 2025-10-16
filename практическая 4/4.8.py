n = int(input("Введите натуральное число n <= 9: "))
for i in range(1, n+1):
    print(''.join(map(str, range(1, i+1))))