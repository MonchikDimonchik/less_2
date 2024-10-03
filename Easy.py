# Родительский класс
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} поехала.")

    def stop(self):
        print(f"{self.name} остановилась.")

    def turn(self, direction):
        print(f"{self.name} повернула {direction}.")


# Дочерние классы
class TownCar(Car):
    pass


class SportCar(Car):
    pass


class WorkCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(60, "Синий", "Городская машина")
sport_car = SportCar(150, "Красный", "Спортивная машина")
work_car = WorkCar(40, "Белый", "Рабочая машина")
police_car = PoliceCar(100, "Чёрный", "Полицейская машина")

town_car.go()
town_car.turn("налево")
town_car.stop()

police_car.go()
police_car.turn("направо")
police_car.stop()