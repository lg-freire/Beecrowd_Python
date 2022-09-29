n = int(input())
s = 0
for i in range(0, n):
    a, b = map(int, input().split())
    if a < b:
        for j in range(a+1, b):
            if j % 2 != 0:
                s += j
        print(s)
    else:
        for j in range(a-1, b, -1):
            if j % 2 != 0:
                s += j
        print(s)
    s = 0
