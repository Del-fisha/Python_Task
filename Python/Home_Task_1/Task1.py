# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

Day = int(input('Введите номер дня недели: '))
if Day < 1 or Day > 7:
    print("Ты ввел неверное число! Срочно извинись и уйди отсюда!")
elif Day > 5:
    print("Это выходной день, отдохни немного")
else:
    print("Это будний день")
