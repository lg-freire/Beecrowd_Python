total = 0
for i in range(0, 2):
    while True:
        n1 = float(input())
        if 0 <= n1 <= 10:
            total += n1
            break
        else:
            print('nota invalida')
print(f'media = {total / 2:.2f}')
