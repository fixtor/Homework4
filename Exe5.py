# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import uFile_IO

get_data1 = str(uFile_IO.Output_data_file('polynomial1.txt', 'r'))
get_data2 = str(uFile_IO.Output_data_file('polynomial2.txt', 'r'))

a = get_data1.replace('[\'', '').replace('= \']', '')
b = get_data2.replace('[\'', '').replace('= \']', '')

print(f'({a}) + ({b})')

uFile_IO.Input_data_file('Summ_of_polynomial.txt', f'({a}) + ({b})', 'w')





