DAY = int(input())
Y = DAY // 365
M = (DAY - Y * 365) // 30
D = DAY - ((Y * 365) + (M * 30))
print("""{} ano(s)
{} mes(es)
{} dia(s)""".format(Y, M, D))
