prof = int(input('Введите выручку фирмы: '))
exp = int(input('Введите издержки фирмы: '))
# prof = int(prof)
# exp = int(exp)
if prof > exp:
  prib = prof - exp
  print(f"Компания получила прибыль = {prib}")
  rent = prib / prof
  print(f"Рентабельность прибыли: {rent}")
  sotr = int(input('Введите количество сотрудников компании: '))
  last = int(prib / sotr)
  print(f"Прибыль фирмы на одного сотрудника: {last}")
else:
  print('Компания понесла убытки')
