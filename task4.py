class Car:
    def __init__(self, speed, color, name, is_police: bool = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        if direction == "Направо":
            print('Машина повернула направо')
        else:
            print('Машина повернула налево')

    def show_speed(self):
        print(f'Скорость машины равна {self.speed} км/ч.')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police: bool = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        if self.speed > 60:
            print('Вы превышаете скорость')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police: bool = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        if self.speed > 40:
            print('Вы превышаете скорость')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police: bool = True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


class SportCar(Car):
    def __init__(self, speed, color, name, is_police: bool = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


town_car = TownCar(70, 'Red', "Ford", False)
work_car = WorkCar(50, 'White', 'Lada', False)
police_car = PoliceCar(90, 'Black', 'Audi', True)
sport_car = SportCar(120, 'Red', 'Bugatti', False)
print(f'Марка городской машины: {town_car.name}\n'
      f'Цвет: {town_car.name}\n'
      f'Скорость {town_car.speed} км/ч\n'
      f'Машина полицеская? {town_car.is_police}')
town_car.show_speed()
print()
print(f'Марка рабочей машины: {work_car.name}\n'
      f'Цвет: {work_car.name}\n'
      f'Скорость {work_car.speed} км/ч\n'
      f'Машина полицеская? {work_car.is_police}')
work_car.show_speed()
print()
print(f'Марка спортивной машины: {sport_car.name}\n'
      f'Цвет: {sport_car.name}\n'
      f'Скорость {sport_car.speed} км/ч\n'
      f'Машина полицеская? {sport_car.is_police}\n\n')
sport_car.show_speed()
print()
print(f'Марка полицеской машины: {police_car.name}\n'
      f'Цвет: {police_car.name}\n'
      f'Скорость {police_car.speed} км/ч\n'
      f'Машина полицеская? {police_car.is_police}\n\n')
police_car.show_speed()
print()
