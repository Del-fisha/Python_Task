# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, Home_Task_5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

array = [2, 3, 5, 9, 3]
sum = 0

for i in range(0, len(array)):
	if i % 2 != 0:
		sum += array[i] 
print(sum)