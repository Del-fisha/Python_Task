# Напишите программу для пересчёта величины временного интервала,
# заданного в минутах, в величину, выраженную в часах и минутах.

minutes = int(input("Введите количество минут: "))

result_hours = minutes // 60
result_minutes = minutes % 60

print("Это" , result_hours , "часов и " , result_minutes , " минут")
