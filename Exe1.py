# Вычислить число c заданной точностью d
#  Пример: - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# задача решена с возможностью округления любой дробной части введенной пользователем

user_input_accuracy = input(f'Введите любое число c количеством знаков после запятой:  ').split('.')
user_input = float(input('Введите число для округления по примеру: '))

accuracy = len([int(x) for x in list(user_input_accuracy[1])]) 

print (f'количественное округление по знакам $d: {accuracy}')
print (f'Округленное число -> {round(user_input, accuracy)}')
