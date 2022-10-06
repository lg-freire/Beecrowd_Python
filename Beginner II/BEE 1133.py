x = int(input())
y = int(input())
if x < y:
    for i in range(x, y):
        if i % 5 == 2 or i % 5 == 3: print(i)
else:
    for i in range(y, x):
        if i % 5 == 2 or i % 5 == 3: print(i)
