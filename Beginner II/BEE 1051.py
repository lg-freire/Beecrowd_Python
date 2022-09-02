wage = float(input())
if wage <= 2000:
    print('Isento')
else:
    if wage <= 3000:
        tax = (wage - 2000) * 0.08
    elif wage <= 4500:
        tax = (1000 * 0.08) + ((wage - 3000) * 0.18)
    elif wage > 4500:
        tax = (1000 * 0.08) + (1500 * 0.18) + ((wage - 4500) * 0.28)
    print('R$ {:.2f}'.format(tax))
