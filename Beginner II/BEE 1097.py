i, j = 1, 7
while i < 10:
    for n in range(0, 3):
        print(f'I={i} J={j}')
        j -= 1
    i += 2
    j += 5
