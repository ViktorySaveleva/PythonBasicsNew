li = list(input('Введите слово: '))
print(li)
i = 1
while i < len(li):
  li[i], li[i - 1] = li[i - 1], li[i]
  print(li)
  i += 2
 