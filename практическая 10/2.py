import os
input_file_name = r'D:\МАГА\современные технологии разработки ПО\практика\практическая 10\Голев_Дмитрий_Юрьевич_Ум252_vvod1.txt'
output_file_name = r'D:\МАГА\современные технологии разработки ПО\практика\практическая 10\Голев_Дмитрий_Юрьевич_Ум252_vivod1.txt'
if not os.path.exists(input_file_name):
    print(f"Файл '{input_file_name}' не найден!")
else:
    with open(input_file_name, 'r') as file:
        lines = file.readlines()
        size = int(lines[0].strip()) 
        matrix = [list(map(float, line.strip().split())) for line in lines[1:size+1]]
    def sd(matrix):
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
    result_matrix = sd(matrix)
    with open(output_file_name, 'w') as out_file:
        for row in result_matrix:
            out_file.write(' '.join(map(lambda x: str(int(x)), row)) + '\n')
    print("Операция выполнена успешно. Результат сохранён в файл:", output_file_name)