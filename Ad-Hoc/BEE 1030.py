nums = []
nc = int(input())
for i in range(0, nc):
    n, k = map(int, input().split())
    for num in range(1, n+1):
        nums.append(num)
    print(nums)
    while len(nums) != 1:
        dead = 0
        if (dead + k) < len(nums):
            dead += k
        else:
            dead = (dead + k) % len(nums)
        del(nums[dead])
        if dead == len(nums):
            dead = 0
    print(f'Case {i+1}: {nums[0]}')
