from math import sqrt
a, b, c = map(float, input().split())
delta = (b ** 2) - 4 * a * c
if a == 0 or delta < 0:
    print('Impossivel calcular')
else:
    R1 = (-b + sqrt(delta)) / (2 * a)
    R2 = (-b - sqrt(delta)) / (2 * a)
    print("""R1 = {:.5f}
R2 = {:.5f}""".format(R1, R2))
