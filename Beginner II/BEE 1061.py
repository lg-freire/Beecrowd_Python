dstart = input()[3:]
hs, ms, ss = map(int, input().split(':'))
dend = input()[3:]
he, me, se = map(int, input().split(':'))
dstart, dend = int(dstart), int(dend)
start = (dstart * 86400) + (hs * 3600) + (ms * 60) + ss
end = (dend * 86400) + (he * 3600) + (me * 60) + se
delta = (end - start)
s = delta % 60
d = delta // 86400
if d > 0:
    delta -= (d * 86400)
h = delta // 3600
if h > 0:
    delta -= (h * 3600)
m = delta // 60
print("""{} dia(s)
{} hora(s)
{} minuto(s)
{} segundo(s)""".format(d, h, m, s))
