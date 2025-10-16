import random
array = [random.randint(-100, 100) for _ in range(10)]
max1 = max(array)
m1 = sum(1 for x in array if x < max1)
m2 = sum(1 for x in array if x > max1)
print("Исходный массив:", array)
print("Максимальный элемент:", max1)
print("Количество элементов меньших максимального:", m1)
print("Количество элементов больших максимального:", m2)