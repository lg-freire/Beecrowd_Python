x = int(input())
y = int(input())
both = [x, y]
s = 0
for i in range(min(both)+1, max(both)):
    if i % 2 != 0:
        s += i
print(s)
