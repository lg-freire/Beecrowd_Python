n = int(input())
c = p1 = 0
p2 = 1
print(c, end=' ')
for i in range(n-1):
    c = p1 + p2
    print(c, end=' ') if i != (n - 2) else print(c)
    p2 = p1
    p1 = c
