# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint, random
with open("file5.txt", "w+", encoding="utf-8") as file5:
    file5.write(" ".join([str(randint(-10, 125)) for _ in range(15)]))
    file5.seek(0)
    print(sum(map(int, file5.readline().split())))


