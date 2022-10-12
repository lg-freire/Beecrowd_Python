s = n = 0
x = int(input())
while True:
    z = int(input())
    if z > x: break
while s < z:
    s += x
    x += 1
    n += 1
print(n)
