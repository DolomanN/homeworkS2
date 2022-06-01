#Найти сумму чисел списка стоящих на нечетной позиции
list = [1,2,3,4]
sum = 0 
for i in list:
    if i % 2 !=0:
        sum = sum + i
print (sum)
