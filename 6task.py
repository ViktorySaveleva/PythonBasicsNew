km = float(input('Введите количество километров, которое Вы пробежали: '))
target = float(input('Введите цель тренировок в километрах: '))
day = 1
print (f" {day}-й день: {round(km, 2)}")
while km < target:
  km = km * 1.1
  day += 1
  print (f" {day}-й день: {round(km, 2)}")
