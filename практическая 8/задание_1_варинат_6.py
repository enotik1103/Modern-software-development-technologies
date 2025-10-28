size = int(input("Введите размер матрицы: "))
matrix = [[0]*size for _ in range(size)]
for i in range(size):
    row = list(map(int, input(f"Введите элементы {i+1}-й строки через пробел: ").split()))
    matrix[i] = row[:size]
max_r = []  
min_r = []  
for row in matrix:
    max_r.append(max(row))  
for i in range(size):
    c = [row[i] for row in matrix]  
    min_r.append(min(c)) 
print("\nМаксимальные элементы строк:")
print(*max_r)
print("\nМинимальные элементы столбцов:")
print(*min_r)