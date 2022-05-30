class Car:
  def __init__(self, speed, color, name, is_police):
    self.speed = speed
    self.color = color
    self.name = name
    self.is_police = is_police

  def go(self):
    print(f'{self.name} поехала')

  def stop(self):
    print(f'{self.name} остановилась')

  def turn_right(self):
    print(f'{self.name} повернула направо')

  def turn_left(self):
    print(f'{self.name} повернула налево')

class TownCar(Car):
  def __init__(self, speed, color, name, is_police):
    super().__init__(speed, color, name, is_police)

  def show_speed(self):
    print(f'Текущая скорость автомобиля {self.name} - {self.speed}')
    if self.speed > 60:
      print(f'Превышение скорости!')
    # if self.is_police == True:
    #   print(f'Это полицейская машина')
    # if self.is_police == False:
    #   print(f'Это не полицейская машина')
    # else:
    #   pass

class SportCar(Car):
  def __init__(self, speed, color, name, is_police):
    super().__init__(speed, color, name, is_police)
    # if self.is_police == True:
    #   print(f'Это полицейская машина')
    # if self.is_police == False:
    #   print(f'Это не полицейская машина')
    # else:
    #   pass

class WorkCar(Car):
  def __init__(self, speed, color, name, is_police):
    super().__init__(speed, color, name, is_police)

  def show_speed(self):
    print(f'Текущая скорость автомобиля {self.name} - {self.speed}')
    if self.speed > 40:
      print(f'Превышение скорости!')
    # if self.is_police == True:
    #   print(f'Это полицейская машина')
    # if self.is_police == False:
    #   print(f'Это не полицейская машина')
    # else:
    #   pass

class PoliceCar(Car):
  def __init__(self, speed, color, name, is_police):
    super().__init__(speed, color, name, is_police)
    # if self.is_police == True:
    #   print(f'Это полицейская машина')
    # if self.is_police == False:
    #   print(f'Это не полицейская машина')
    # else:
    #   pass
    
volvo = TownCar(70, 'red', 'Volvo', False)
maclaren = SportCar(100, 'blue', 'Maclaren', False)
lada = WorkCar(30, 'white', 'Lada', False)
police = PoliceCar(40, 'green', 'Police', True)
print(lada.turn_left())
print(volvo.stop())
print(maclaren.go())
print(police.turn_right())
print(lada.show_speed())
print(volvo.show_speed())