class Stationery:
  title = ''

  def draw(self):
    print(f'Запуск отрисовки')

class Pen(Stationery):
  def draw(self):
    print(f'Запуск отрисовки ручкой')
class Pencil(Stationery):
  def draw(self):
    print(f'Запуск отрисовки карандашом')
class Handle(Stationery):
  def draw(self):
    print(f'Запуск отрисовки маркером')

a = Pen()
a.draw()
b = Pencil()
b.draw()
c = Handle()
c.draw()