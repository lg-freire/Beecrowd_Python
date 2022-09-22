nc = int(input())
for i in range(0, nc):
    n, k = map(int, input().split())
    nums = list(range(1, n+1))
    print(nums)
    dead = k - 1
    while len(nums) > 1:
        nums.pop(dead)
        dead += (k - 1)
        if dead >= len(nums):
            dead %= len(nums)
        print(nums)
    print(f'Case {i+1}: {nums[0]}')
