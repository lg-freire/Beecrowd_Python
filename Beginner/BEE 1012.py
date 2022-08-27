A, B, C = map(float, input().split())
RT = (A * C) / 2
CI = 3.14159 * pow(C, 2)
T = ((A + B) / 2) * C
S = pow(B, 2)
RE = A * B
print("""TRIANGULO: {:.3f}
CIRCULO: {:.3f}
TRAPEZIO: {:.3f}
QUADRADO: {:.3f}
RETANGULO: {:.3f}""".format(RT, CI, T, S, RE))
