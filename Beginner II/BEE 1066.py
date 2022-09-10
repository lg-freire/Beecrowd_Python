e = o = p = n = 0
for i in range(0, 5):
    en = int(input())
    if en % 2 == 0:
        e += 1
    else:
        o += 1
    if en > 0:
        p += 1
    elif en < 0:
        n += 1
print("""{} valor(es) par(es)
{} valor(es) impar(es)
{} valor(es) positivo(s)
{} valor(es) negativo(s)""".format(e, o, p, n))
