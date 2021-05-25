li = str(input('Введите несколько слов через пробел: '))
li = list(li.split(' '))
for index, item in enumerate(li):
  print(index + 1, item)