# Сгенерируйте список на 30 элементов. 
# Отсортируйте список по возрастанию, методом сортировки выбором.

import random


def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]


a = int(input("Введите минимальное значение списка: "))
b = int(input("Введите максимальное значение списка: "))
array = []
for i in range(30):
    x = random.randint(a, b)
    array.append(x)

print("Случайный массив: ")
print(array)
print()
selection_sort(array)
print("Отсортированный массив: ")
print(array)
