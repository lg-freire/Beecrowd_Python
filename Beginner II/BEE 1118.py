while True:
    flag = 0
    total = 0
    for i in range(0, 2):
        while True:
            n = float(input())
            if 0 <= n <= 10:
                total += n
                break
            else:
                print('nota invalida')
    print(f'media = {total / 2:.2f}')
    while 1 >= flag >= 2:
        flag = int(input('novo calculo (1-sim 2-nao)'))
    if flag == 2:
        break
