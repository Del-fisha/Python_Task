# Вводим с клавиатуры десятичное число. Необходимо
# перевести его в шестнадцатеричную систему счисления.

num = int(input("Введите число: "))
string = ''
system = '0123456789ABCDEF'

while num > 0:
    string = system[num % 16] + string
    num = num // 16

print(string)