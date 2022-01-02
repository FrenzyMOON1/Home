# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open("file1.txt", "r", encoding="utf-8") as l_calc:
    file1 = l_calc.readlines()
    for i, k in enumerate(file1, 1):
        print(f'{i} строка - {len(k.split())} слова(ов) - {len(k)-1} - элемнента(ов)')
