x, y = map(int, input().split())
count = 0
for i in range(1, y+1):
    print(i, end='')
    count += 1
    if count == x:
        print()
        count = 0
    else: print(' ', end='')
