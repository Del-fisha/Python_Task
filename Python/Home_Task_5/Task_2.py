# Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
# И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)

import random



def create_array():
	array_a = int(input("Введите количество столбцов: "))
	array_b = int(input("Введите количество строк: "))
	array=[]
	s =[]
	for i in range(array_b):
		array_2 = []
		sum=0
		for j in range(array_a):
			n=random.randint(0, 9)
			array_2.append(n)
			sum += n / array_a
		array.append(array_2)
		print(array_2)
		s.append(round(sum,1))
	print("Среднее арифметическое каждой строки: ")	
	print(s)

create_array()
