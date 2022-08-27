# https://www.beecrowd.com.br/judge/en/problems/view/1021
V = float(input())
N100, N50, N20, N10, N5, N2 = 0, 0, 0, 0, 0, 0
M100, M50, M25, M10, M5, fuckbeecrowd = 0, 0, 0, 0, 0, 0
if V // 100 > 0:
    N100 = int(V // 100)
    V = V - ((V // 100) * 100)
if V // 50 > 0:
    N50 = int(V // 50)
    V = V - ((V // 50) * 50)
if V // 20 > 0:
    N20 = int(V // 20)
    V = V - ((V // 20) * 20)
if V // 10 > 0:
    N10 = int(V // 10)
    V = V - ((V // 10) * 10)
if V // 5 > 0:
    N5 = int(V // 5)
    V = V - ((V // 5) * 5)
if V // 2 > 0:
    N2 = int(V // 2)
    V = V - ((V // 2) * 2)
V = V * 100
if V // 100 > 0:
    M100 = int(V // 100)
    V = V - ((V // 100) * 100)
if V // 50 > 0:
    M50 = int(V // 50)
    V = V - ((V // 50) * 50)
if V // 25 > 0:
    M25 = int(V // 25)
    V = V - ((V // 25) * 25)
if V // 10 > 0:
    M10 = int(V // 10)
    V = V - ((V // 10) * 10)
if V // 5 > 0:
    M5 = int(V // 5)
    V = V - ((V // 5) * 5)
if V // 1 > 0:
    fuckbeecrowd = V // 1
print("""NOTAS:
{} nota(s) de R$ 100.00
{} nota(s) de R$ 50.00
{} nota(s) de R$ 20.00
{} nota(s) de R$ 10.00
{} nota(s) de R$ 5.00
{} nota(s) de R$ 2.00
MOEDAS:
{} moeda(s) de R$ 1.00
{} moeda(s) de R$ 0.50
{} moeda(s) de R$ 0.25
{} moeda(s) de R$ 0.10
{} moeda(s) de R$ 0.05
{:.0f} moeda(s) de R$ 0.01""".format(N100, N50, N20, N10, N5, N2, M100, M50, M25, M10, M5, fuckbeecrowd))
