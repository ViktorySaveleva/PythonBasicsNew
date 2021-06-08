# Не поняла где ошибка и окончательно запуталась
my_str = input('Введите несколько чисел через пробел, для выхода - !: ')
def sum_numb(my_str):
  global y, res, listStr, res1, res2
  y = True
  res = 0
  res1 = 0
  while y:
    if my_str[-1] == '!':
      y = False
      listStr = list(my_str.split(' '))
      listStr.pop(-1)
      my_str = ''.join(listStr)
      my_str = list(my_str)
      my_str = [int(i) for i in my_str]
      res = [res + i for i in my_str]
      break
    else:
      my_str = list(my_str.split(' '))
      my_str = [int(i) for i in my_str]
      res = [res + i for i in my_str]
      res1 = res
      my_str = input('Введите несколько чисел, для выхода - !: ')
      my_str = list(my_str.split(' '))
      my_str = [int(i) for i in my_str]
      res = [res + i for i in my_str]
      res = res1 + res
      res2 = res
  return res, res2
print(sum_numb(my_str))



