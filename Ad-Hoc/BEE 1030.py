
nc = int(input())
for i in range(0, nc):
    n, k = map(int, input().split())
    nums = list(range(1, n+1))
    print(nums)
    dead = 0
    while len(nums) > 1:
        if (dead + k) <= len(nums):
            dead += k
        else:
            dead = (dead + k) % len(nums)
        if dead != 0:
            del nums[dead-1]
        else:
            del nums[dead]
        print(nums)
        if dead == len(nums):
            dead = 0
    print(f'Case {i+1}: {nums[0]}')
