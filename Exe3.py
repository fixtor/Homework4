# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from uCreate_user_list import Int_list_create

new_list = Int_list_create()
new_list1 = []

for x in new_list:
    if new_list.count(x) == 1:
         new_list1.append(x)

print(new_list)
print(new_list1)
