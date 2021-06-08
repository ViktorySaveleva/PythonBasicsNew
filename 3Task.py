ar1 = int(input('Введите первое число: '))
ar2 = int(input('Введите второе число: '))
ar3 = int(input('Введите третье число: '))
def my_func(ar1, ar2, ar3): 
  if ar1 < ar2 and ar1 < ar3:
    return ar2 + ar3
  elif ar2 < ar1 and ar2 < ar3:
    return ar1 + ar3
  else:
    return ar1 + ar2
print(my_func(ar1, ar2, ar3))