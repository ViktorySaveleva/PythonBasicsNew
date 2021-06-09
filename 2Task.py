class Road:
  _length = 0
  _width = 0

  def __init__(self, _length, _width):
    m1 = 25
    t = input('Введите желаемую толщину полотна в сантиметрах: ')
    t = int(t)
    t = t * 0.01
    m = _length * _width * m1 * t
    m = int(m)
    print(f'Вам понадобится {m} килограммов')
road = Road(20, 5000)
road2 = Road(10, 3000)



  