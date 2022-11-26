count = int(input("Введите зарплату: "))

rouble_25 = 0
rouble_10 = 0
rouble_3 = 0
rouble_1 = 0

while count >= 25:
    count -= 25
    rouble_25 += 1
while count >= 10:
    count -= 10
    rouble_10 += 1
while count >= 3:
    count -= 3
    rouble_3 += 1
while count >= 1:
    count -= 1
    rouble_1 += 1


print(f"Минимальное количество купюр в зарплате: {rouble_25 + rouble_10 + rouble_3 + rouble_1}")
print(f"Из них: 25р. - {rouble_25} шт,10р. - {rouble_10} шт,3р. - {rouble_3} шт,1р. - {rouble_1} шт,")
