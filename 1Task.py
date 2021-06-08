from sys import argv
ar1, ar2, ar3 = map(int, argv[1:])
res = (ar1 * ar2) + ar3
print(f"Ваша заработная плата составляет {res}")