sec = input('Введите количество секунд: ')
sec = int(sec)
hour = sec // 3600
#print(hour)
sec2 = sec % 3600
#print(sec2)
min = sec2 // 60
#print(min)
sec3 = sec2 % 60
#print(sec3)
print(f"{hour}:{min}:{sec3}")
