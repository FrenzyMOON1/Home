def top_two(a, b, c):
    max_2 = 0
    max_1 = max(a, b, c)
    if max_1 == a:
        max_2 = max(b, c)
    if max_1 == b:
        max_2 = max(c, a)
    if max_1 == c:
        max_2 = max(a, b)

    return f'Сумма двух самых больших элементов: {max_1 + max_2}, '


print("Введите 3 числа через Enter: ")
print(top_two(int(input()), int(input()), int(input())))
