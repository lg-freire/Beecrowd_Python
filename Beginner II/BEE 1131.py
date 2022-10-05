total = inter = gr = draw = 0
while True:
    x, y = map(int, input().split())
    total += 1
    if x == y: draw += 1
    elif x > y: inter += 1
    else: gr += 1
    print('Novo grenal (1-sim 2-nao)')
    flag = int(input())
    if flag == 2:
        break
print(f"""{total} grenais
Inter:{inter}
Gremio:{gr}
Empates:{draw}""")
if inter == gr:
    print('Não houve vencedor')
else:
    print('Inter venceu mais') if inter > gr else print('Gremio venceu mais')
