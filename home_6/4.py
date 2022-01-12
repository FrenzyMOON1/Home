from random import choice


class Car:
    direction = ["North", "South", "West", "East"]

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name}: машина в движении!')

    def stop(self):
        print(f'{self.stop}: машина остановилась!')

    def turn(self):
        print(f'{self.turn}: машина повернула на {choice(self.direction)}.')

    def show_speed(self):
        return f'{self.name} = скорость: {self.speed} км/ч'


class TownCar(Car):

    def show_speed(self):
        return f'{self.name}= скорость: {self.speed} превышение скоростного режима!' \
            if self.speed > 60 else super().show_speed()


class WorkCar(Car):

    def show_speed(self):
        return f'{self.name} = скорость: {self.speed} превышение скоростного режима!' \
            if self.speed > 40 else super().show_speed()


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=True)
        self.is_police = is_police


police_car = PoliceCar(90, "Голубой", "Бобик")
work_car = WorkCar(30, "Черный", "Хендай")
town_car = TownCar(65, "Белый", "Мерседес")

list_of_cars = [police_car, work_car, town_car]

for i in list_of_cars:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()
