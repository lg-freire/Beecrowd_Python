C = int(input())
for X in range(C):
    N, M = map(int, input().split())
    D = str(N ** M)
    print(len(D))
