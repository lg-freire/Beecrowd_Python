n = int(input())
c = r = s = 0
for i in range(0, n):
    num, anim = map(str, input().upper().split())
    if anim == 'C':
        c += int(num)
    elif anim == 'R':
        r += int(num)
    elif anim == 'S':
        s += int(num)

total = c + r + s
print(f"""Total: {total} cobaias
Total de coelhos: {c}
Total de ratos: {r}
Total de sapos: {s}
Percentual de coelhos: {(c * 100) / total:.2f} %
Percentual de ratos: {(r * 100) / total:.2f} %
Percentual de sapos: {(s * 100) / total:.2f} %""")
