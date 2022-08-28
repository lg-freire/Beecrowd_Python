T = int(input())
H = T // 3600
M = (T - H * 3600) // 60
print('{}:{}:{}'.format(H, M, T % 60))
