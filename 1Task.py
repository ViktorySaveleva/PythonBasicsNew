ar1 = float(input('Введите первое число: '))
ar2 = float(input('Введите второе число: '))
def div(ar1, ar2):
  global res
  if ar2 == 0:
    print('На ноль делить нельзя')
    ar2 = float(input('Введите второе число: '))
    res = ar1 / ar2
    return res
  else:
    res = ar1 / ar2
    return res
print(div(ar1, ar2))