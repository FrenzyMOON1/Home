def calculat(a, b):
    print("Введите 2 числа: ")
    a, b = (int(input()), int(input()))
    if b != 0:
        return a / b
    else:
        return "Error"


print(calculat(0, 0))
print(calculat(0, 0))
