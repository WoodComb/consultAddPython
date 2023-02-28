start, end = 2000, 3200
a = [i for i in range(start, end) if i%7 == 0 and i%5 != 0]
print(a)