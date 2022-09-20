# Lists start being used here

n = int(input())
li, liw = [], []
for i in range(0, n):
    x = int(input())
    if x in range(10, 21):
        li.append(x)
    elif x < 0:
        x = None
    else:
        liw.append(x)
print(f'{len(li)} in')
print(f'{len(liw)} out')
