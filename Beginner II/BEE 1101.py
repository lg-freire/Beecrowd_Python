s = 0
while True:
    m, n = map(int, input().split())
    if m <= 0 or n <= 0:
        break
    if m < n:
        for i in range(m, n+1):
            print(i, end=' ')
            s += i
        print(f'Sum={s}')
    else:
        for i in range(n, m+1):
            print(i, end=' ')
            s += i
        print(f'Sum={s}')
    s = 0
