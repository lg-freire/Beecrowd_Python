n = int(input())
for i in range(0, n):
    num = int(input())
    if num == 0:
        print('NULL')
    else:
        if num % 2 != 0:
            print('ODD', end=' ')
        else:
            print('EVEN', end=' ')
        if num < 0:
            print('NEGATIVE')
        else:
            print('POSITIVE')
