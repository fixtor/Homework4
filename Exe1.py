# Вычислить число c заданной точностью d
#  Пример: - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

user_input = float(input(f'Введите любое вещественное число в диапазоне от: {10**(-1)} до {10**(-10)} '))
accuracy = int(input('Введите округление: '))
if (user_input >= 10**(-10) and user_input <= 10**(-1)):
    print(round(user_input, accuracy))
else:
    print(f'введенные данные {user_input} не верные')






