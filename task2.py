#Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
#Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

list = [2, 3, 4, 5, 6]
i=0
j = -1
temp = 0
new_list = []
while i < len(list)/2:
   temp = list[i] * list[j]
   i = i+1
   j = j-1
   print (temp)
   new_list.append(temp)
print (new_list)

