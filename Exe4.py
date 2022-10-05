from random import *
from uFile_IO import *

k=2

coefficient_a = round(random()*100, )
coefficient_b = round(random()*100, )
coefficient_c = round(random()*100, )

print(coefficient_a, coefficient_b, coefficient_c)
result = ''
if coefficient_b == 0:
    result = f"{coefficient_a}*x^{k} + {coefficient_c}*x^{k-2} = 0"
if coefficient_b == 0 and coefficient_c == 0: result =  f"{coefficient_a}*x^{k} = 0"
else: result =  f"{coefficient_a}*x^{k} + {coefficient_b}*x^{k-1} + {coefficient_c}*x^{k-2} = 0 "

Input_data_file('test.txt', result, 'w')
