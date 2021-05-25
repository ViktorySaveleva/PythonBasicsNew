my_list = [9, 6, 5, 3, 3, 1]
el = int(input('Введите натуральное число: '))
for i in range(len(my_list)):
  if my_list[i] == el:
    my_list.insert(i + 1, el)
    break
  elif my_list[0] < el:
    my_list.insert(0, el)
  elif my_list[-1] > el:
    my_list.append(el)
  elif my_list[i] > el and my_list[i + 1] < el:
    my_list.insert(i + 1, el)
print(my_list)