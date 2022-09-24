x, y, z = map(int, input().split())
li = [x, y, z]
if x != max(li) and x != min(li):
    print('huguinho')
elif y != max(li) and y != min(li):
    print('zezinho')
else:
    print('luisinho')
