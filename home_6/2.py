class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asd(self, wes=25, tol=5):
        return f'{self._width} метров * {self._length} метров * {wes} кг * {tol} см = ' \
               f'{(self._width * self._length * wes * tol) / 1000} тонн'


road1 = Road(20000, 10)
print(road1.asd())
