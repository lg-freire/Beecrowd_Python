n = int(input())
for i in range(0, n):
    x, y = map(int, input().split())
    try:
        print(f'{x / y:.1f}')
    except ZeroDivisionError:
        print('divisao impossivel')
