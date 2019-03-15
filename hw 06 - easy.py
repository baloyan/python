# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
# о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class Car:
    def __init__(self, speed, color, name):
        self.speed  = speed
        self.color = color
        self.name = name

    def car_go(self):
        print('Машина {} начала свое движение!'.format(self.name))

    def car_stop (self):
        print('Машина {} остановилась!'.format(self.name))

    def car_turn (self, direction):
        print('Машина {} повернула {}!'.format(self.name, direction))


class TownCar(Car):
    def __init__ (self, speed, color, name):
        Car.__init__(self,speed,color,name)

class SportCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name)

class WorkCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police = True):
        Car.__init__(self, speed, color, name)
        self.is_police = is_police


my_car = Car(300,'Grey','BMW')

my_car.car_go()
my_car.car_turn('Налево')
my_car.car_stop()

