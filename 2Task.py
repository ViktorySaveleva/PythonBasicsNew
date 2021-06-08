lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_lst = [el for i, el in enumerate(lst) if lst[i] > lst[i - 1] and i > 1]
print(new_lst)