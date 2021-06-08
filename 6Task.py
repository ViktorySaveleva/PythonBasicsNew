
my_str = input('Введите несколько слов через пробел: ')
def int_func(my_str):
  list(my_str.split(' '))
  my_str = my_str.title()
  return my_str
print(int_func(my_str))