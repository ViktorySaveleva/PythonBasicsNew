# Первый вариант
x = int(input('Введите целое положительное число: '))
y = int(input('Введите целое отрицательное число: '))
def my_func(x, y):
  return x ** (abs(y))
print(my_func(x, y))
# Второй вариант
x = int(input('Введите целое положительное число: '))
y = int(input('Введите целое отрицательное число: '))
def my_func(x, y):
  global res
  i = 1
  res = 1
  while i <= abs(y):
    res *= x
    i += 1
  return res
print(my_func(x, y))

