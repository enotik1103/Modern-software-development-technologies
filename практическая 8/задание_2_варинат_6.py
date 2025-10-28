def input_matrix():
    while True:
        try:
            n = int(input("Введите размер матрицы: "))
            if n % 2 != 1:
                print("Размер матрицы должен быть нечетным числом.")
                continue
            break
        except ValueError:
            print("Ошибка ввода. Попробуйте снова.")
        matrix = []
    for i in range(n):
        while True:
            try:
                row1 = list(map(float, input(f"Введите {n} чисел для строки {i+1}: ").split()))
                if len(row1) != n:
                    print(f"Нужно ввести ровно {n} числа.")
                    continue
                matrix.append(row1)
                break
            except ValueError:
                print("Ошибка ввода. Используйте только числа.")      
    return matrix
def sd (matrix):
    n = len(matrix)
    if n % 2 != 1 or any(len(row) != n for row in matrix):
        raise ValueError("Матрица должна быть квадратной с нечетным порядком")
    max_v = float('-inf')
    max_p = None
    for i in range(n):
        md = matrix[i][i]
        sd = matrix[i][n - 1 - i]
        if md > max_v:
            max_v = md
            max_p = (i, i)
        if sd > max_v:
            max_v = sd
            max_p = (i, n - 1 - i)
    c1 = c2 = n // 2
    if max_p == (c1, c2):
        return matrix
    temp = matrix[max_p[0]][max_p[1]]
    matrix[max_p[0]][max_p[1]] = matrix[c1][c2]
    matrix[c1][c2] = temp
    return matrix
if __name__ == "__main__":
    matrix = input_matrix()
    result_m = sd(matrix)
    print("\nПреобразованная матрица:")
    for row in result_m:
        print(' '.join(map(lambda x: str(int(x)), row)))
