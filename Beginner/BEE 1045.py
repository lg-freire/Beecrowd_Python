a, b, c = map(float, input().split())
if a < b:
    b1 = a
    a = b
    b = b1
if a < c:
    c1 = a
    a = c
    c = c1
if b < c:
    b1 = b
    b = c
    c = b1
if a >= b + c:
    print('NAO FORMA TRIANGULO')
else:
    if (a ** 2) == (b ** 2) + (c ** 2):
        print('TRIANGULO RETANGULO')
    if (a ** 2) > (b ** 2) + (c ** 2):
        print('TRIANGULO OBTUSANGULO')
    if (a ** 2) < (b ** 2) + (c ** 2):
        print('TRIANGULO ACUTANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    if a == b != c or b == c != a or a == c != b:
        print('TRIANGULO ISOSCELES')
