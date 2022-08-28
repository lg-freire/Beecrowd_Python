N = int(input())
V = N
N100, N50, N20, N10, N5, N2, N1 = 0, 0, 0, 0, 0, 0, 0
if V // 100 > 0:
    N100 = int(V // 100)
    V -= (V // 100) * 100
if V // 50 > 0:
    N50 = int(V // 50)
    V -= (V // 50) * 50
if V // 20 > 0:
    N20 = int(V // 20)
    V -= (V // 20) * 20
if V // 10 > 0:
    N10 = int(V // 10)
    V -= (V // 10) * 10
if V // 5 > 0:
    N5 = int(V // 5)
    V -= (V // 5) * 5
if V // 2 > 0:
    N2 = (V // 2)
    V -= (V // 2) * 2
if V / 1 >= 0:
    N1 = int(V / 1)
print("""{}
{} nota(s) de R$ 100,00
{} nota(s) de R$ 50,00
{} nota(s) de R$ 20,00
{} nota(s) de R$ 10,00
{} nota(s) de R$ 5,00
{} nota(s) de R$ 2,00
{} nota(s) de R$ 1,00""".format(N, N100, N50, N20, N10, N5, N2, N1))
