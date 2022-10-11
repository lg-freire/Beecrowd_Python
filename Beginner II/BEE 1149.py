x = input().split()
a = int(x[0])
n = int(x[-1])
s = 0
for i in range(n):
    s += a + i
print(s)
