# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

number = int(input("Введите число:"))
new_list = []     
div = 2
while(div <= number):
    if (number % div ==0):
        new_list.append(div)
        number = number/div
    else:
        div += 1 
print (new_list)
        

        


