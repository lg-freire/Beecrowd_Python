def fibonacci(n):
    c = n1 = 0
    n2 = 1
    print(c, end=' ')
    for i in range(n-1):
        c = n1 + n2
        print(c, end=' ') if i != (n -2) else print(c)
        n2 = n1
        n1 = c


x = int(input())
fibonacci(x)
