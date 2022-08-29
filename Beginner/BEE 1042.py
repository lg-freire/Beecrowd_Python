x, y, z = map(int, input().split())
if x < y < z:
    print('''{}
{}
{}'''.format(x, y, z))
elif x < z < y:
    print('''{}
{}
{}'''.format(x, z, y))
elif y < x < z:
    print('''{}
{}
{}'''.format(y, x, z))
elif y < z < x:
    print('''{}
{}
{}'''.format(y, z, x))
elif z < x < y:
    print('''{}
{}
{}'''.format(z, x, y))
elif z < y < x:
    print('''{}
{}
{}'''.format(z, y, x))
print('''
{}
{}
{}'''.format(x, y, z))
