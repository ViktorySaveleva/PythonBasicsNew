
from itertools import count

for el in count(1):
  if el > 10:
    break
  else:
    print(el)

from itertools import cycle
lst = ['fcd', '5', 'hgb', '6']
c = 0
for el in cycle(lst):
  if c > 5:
    break
  else:
    print(el)
    c += 1
