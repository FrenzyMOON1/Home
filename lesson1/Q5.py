izd = int(input("Издержки фирмы: "))
vir = int(input("Выручка фирмы: "))
rent = 0
if vir > izd:
    print("Ваша фирма приносит прибыль, так держать!")
    rent = (vir - izd) / vir * 100
    print("Рентабильность вашей фирмы: ", rent)
elif vir == izd:
    print("Фаша фирма работает в 0")
else:
    print("Ваша фирма приносит убыток.")

rab = int(input('Введите число ваших сотрудников: '))
p_r = (vir - izd) / rab
print('Прибыль фирмы на одного работника = ', p_r)
