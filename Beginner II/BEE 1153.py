def factorial(n):
    for i in range(n, 1, -1):
        n *= (i - 1)
    return n


x = int(input())
print(factorial(x))
