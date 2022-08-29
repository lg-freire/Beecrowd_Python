x, y = map(int, input().split())
if x == y:
    print('O JOGO DUROU 24 HORA(S)')
elif x > y:
    print('O JOGO DUROU {:.0f} HORA(S)'.format((y - x) + 24))
elif y > x:
    print('O JOGO DUROU {:.0f} HORA(S)'.format(y - x))
