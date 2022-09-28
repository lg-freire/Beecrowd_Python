i, j = 0, 1
while i < 2:
    for n in range(0, 3):
        print(f'I={i:g} J={j:g}')
        j += 1
    i += 0.2
    j -= 3
    j += 0.2
