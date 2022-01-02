from time import sleep


class TrafficLight:
    __color = "Серый"

    def running(self):
        while True:
            print("Светофор зеленый сейчас")
            sleep(1)
            print("Светофор желтый сейчас")
            sleep(2)
            print("Светофор красный сейчас")
            sleep(7)
            print("Светофор желтый сейчас")
            sleep(2)


a = TrafficLight()
a.running()
