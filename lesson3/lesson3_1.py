def calculat(a, b):
    if b != 0:
        return a / b
    else:
        return "Error"


print("Введите 2 числа: ")
print(calculat(int(input()), int(input())))
print(calculat(int(input()), int(input())))
