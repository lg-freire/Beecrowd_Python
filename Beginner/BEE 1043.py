x, y, z = map(float, input().split())
if (x + y) > z and (x + z) > y and (z + y) > x:
    print('Perimetro = {:.1f}'.format(x + y + z))
else:
    print('Area = {:.1f}'.format(((x + y) / 2) * z))
