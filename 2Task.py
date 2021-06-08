user = {  
  'name': input('Введите Ваше имя: '),
  'surname': input('Введите Вашу фамилию: '),
  'birth_year': input('Введите Ваш год рождения: '),
  'city': input('Введите Ваш город проживания: '),
  'email': input('Введите Ваш email: '),
  'phone': input('Введите Ваш номер телефона: ')
      }
def print_user_data(user):
  print(f'Имя: {user.get("name")}, фамилия: {user.get("surname")},'
  f' год рождения: {user.get("birth_year")}, город проживания: {user.get("city")},'
  f' email: {user.get("email")}, телефон: {user.get("phone")}')

print_user_data(user)

