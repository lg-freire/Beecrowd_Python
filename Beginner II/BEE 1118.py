while True:
    x = 0
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
    while x != 1 and x != 2:
        # URI só aceita assim
        print('novo calculo (1-sim 2-nao)')
        x = int(input())
    if x == 2:
        break
