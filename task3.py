#В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
#Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]

temp = 0 
max = list[0]
min = list[0]
for i in list:
    if i % 1 != 0 and  i % 1 > max%1:
        max = i
    if i % 1 != 0 and  i % 1 < min%1:
        min = i
temp = (max - int(max)) - (min - int (min))
print (round(temp,3))