# Вводим с клавиатуры строку. Необходимо сказать,
# является ли эта строка дробным числом

num = float(input("Введите число: "))
print(f'{num} - число { ["дробное","целое"][ num.is_integer() ] }')
