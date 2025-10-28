import os
input_file_name = r'D:\МАГА\современные технологии разработки ПО\практика\практическая 10\Голев_Дмитрий_Юрьевич_Ум252_vvod.txt'
output_file_name =  r'D:\МАГА\современные технологии разработки ПО\практика\практическая 10\Голев_Дмитрий_Юрьевич_Ум252_vivod.txt'
if not os.path.exists(input_file_name):
    print(f"Файл '{input_file_name}' не найден!")
else:
 with open(input_file_name, 'r', encoding='utf-8') as file:
    size = int(file.readline().strip())  
    matrix = []
    for _ in range(size):
        row = list(map(int, file.readline().strip().split()))  
        matrix.append(row)
 max_r = [max(row) for row in matrix]
 min_r = [min([row[i] for row in matrix]) for i in range(size)]
 result_str = f'Max element:\n{" ".join(map(str, max_r))}\n\nMin element:\n{" ".join(map(str, min_r))}'
 with open(output_file_name, 'w') as output_file:
    output_file.write(result_str)
 print("Данные успешно обработаны и сохранены в файле:", output_file_name)