t = s = 0
for i in range (0, 6):
    n = float(input())
    if n > 0:
        t += 1
        s += n
av = s / t
print('''{} valores positivos
{:.1f}'''.format(t, av))
