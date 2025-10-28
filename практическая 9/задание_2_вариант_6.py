def n(max1=None, max2=None):
    num = int(input("Введите натуральные числа, закончите ввод 0: "))
    if num == 0:
        if max2 is not None:
            print(max2)
        else:
            print("Последовательность некорректна")
    else:
        if max1 is None or num >= max1:
            max2 = max1
            max1 = num 
        elif max2 is None or num > max2:
            max2 = num 
        n(max1, max2)
n()