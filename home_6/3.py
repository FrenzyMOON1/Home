class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = f"Должность - {position}"
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"Имя - {self.name}, Фамилия - {self.surname}"

    def get_full_profit(self):
        return f"Доход - {sum(self._income.values())}"


a = Position("Yarik", "Hamburger", "Director", 20000, 5000)
print(a.get_full_name())
print(a.get_full_profit())
print(a.position)
