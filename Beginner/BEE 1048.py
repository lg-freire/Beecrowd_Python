pay = float(input())
if pay <= 400:
    r = pay * 1.15
    print("""Novo salario: {:.2f}
Reajuste ganho: {:.2f}
Em percentual: 15 %""".format(r, r - pay))
elif 400 < pay <= 800:
    r = pay * 1.12
    print("""Novo salario: {:.2f}
Reajuste ganho: {:.2f}
Em percentual: 12 %""".format(r, r - pay))
elif 800 < pay <= 1200:
    r = pay * 1.1
    print("""Novo salario: {:.2f}
Reajuste ganho: {:.2f}
Em percentual: 10 %""".format(r, r - pay))
elif 1200 < pay <= 2000:
    r = pay * 1.07
    print("""Novo salario: {:.2f}
Reajuste ganho: {:.2f}
Em percentual: 7 %""".format(r, r - pay))
else:
    r = pay * 1.04
    print("""Novo salario: {:.2f}
Reajuste ganho: {:.2f}
Em percentual: 4 %""".format(r, r - pay))
