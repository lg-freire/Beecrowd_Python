nums = []
nc = int(input())
for i in range(0, nc):
    n, k = map(int, input().split())
    for num in range(1, n+1):
        nums.append(num)
    print(nums)
    while True:
        if len(nums) == 1:
            break
        for dead in range(1, len(nums)+1, k):
            nums.remove(dead)
    print(f'Case {i+1}: {nums[0]}')
