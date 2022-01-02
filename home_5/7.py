import json

with open("json.text_7.txt", "w", encoding='utf-8') as j_file7:
    with open("text_7.txt", "r", encoding="utf-8") as file7:
        pribil = {i.split()[0]: int(i.split()[2]) - int(i.split()[3]) for i in file7}
        result = [pribil, {"Средняя прибыль ": round(sum([int(a) for a in pribil.values() if int(a) > 0]) /
                                                     len([int(a) for a in pribil.values() if int(a) > 0]))}]

    json.dump(result, j_file7, ensure_ascii=False, indent=5)
