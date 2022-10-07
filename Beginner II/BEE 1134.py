a = g = d = 0
while True:
    choice = int(input())
    while 1 > choice or choice > 4:
        choice = int(input())
    # print(f'pick {choice}')
    if choice == 1: a += 1
    elif choice == 2: g += 1
    elif choice == 3: d += 1
    elif choice == 4: break
print(f"""MUITO OBRIGADO
Alcool: {a}
Gasolina: {g}
Diesel: {d}""")
