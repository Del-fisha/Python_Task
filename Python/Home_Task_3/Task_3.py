# Вводим с клавиатуры строку. Необходимо вывести строку,
# где развернём подстроку между первой и последней буквой
# "о" из исходной строки. Если она только одна или её нет - то сообщить,
# что буква "о" - одна или не встречается.

s = str(input("Введите текст: "))
n = len(s)
start = s.find("o")
end = s.rfind("o")
substring = ''
print(s)
if s.count("o") <= 1:
    print("Буква 'о' - одна или не встречается")
else:
    for i in range(end -1, start, -1):
        substring += s[i]
print(substring)