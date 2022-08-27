a, b, c = map(int, input().split())
MAB = int((a + b + abs(a - b)) / 2)
if MAB > c:
    print('{} eh o maior'.format(MAB))
else:
    print('{} eh o maior'.format(c))
