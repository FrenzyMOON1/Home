# Необходимо написать программу,
# открывающую файл на чтениеи считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
from googletrans import Translator

with open("new_text_4.txt", "w+", encoding="utf-8") as new_slo:
    with open("text_4.txt", "r", encoding="utf-8") as slo:
        file1 = slo.read()
        new_slo.write(Translator().translate(file1, dest='ru').text)
        new_slo.seek(0)
        print(new_slo.read())