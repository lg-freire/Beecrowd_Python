x = input().split()
a = int(x[0])
n = int(x[-1])
for i in range(0, n-1):
    a += (a + 1)
print(a)
