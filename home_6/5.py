class Stationery:
    def __init__(self, title="Можно рисовать -"):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print(f"Игрок начинает рисовать {self.title} ручкой")

class Pencil(Stationery):
    def draw(self):
        print(f"Игрок начинает рисовать {self.title} карандашом")

class Handle(Stationery):
    def draw(self):
        print(f"Игрок начинает рисовать {self.title} маркером")

stat = Stationery()
pen = Pen("кривой")
pencil = Pencil("большим")
handle = Handle("грязным")

x = [stat, pen, pencil, handle]
for i in x:
    i.draw()
