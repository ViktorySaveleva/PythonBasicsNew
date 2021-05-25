# list
li = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
month = int(input('Введите номер месяца от 1 до 12: '))
if month == li[0] or month == li[1] or month == li[2]:
  print('Это зима')
elif month == li[3] or month == li[4] or month == li[5]:
  print('Это весна')
elif month == li[6] or month == li[7] or month == li[8]:
  print('Это лето')
elif month == li[9] or month == li[10] or month == li[11]:
  print('Это осень')
else:
  print('Такого месяца нет')

  
# dict
li = {12: 'Зима', 1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень', 10: 'Осень', 11: 'Осень'}
month = int(input('Введите номер месяца от 1 до 12: '))
print(li.get(month))


