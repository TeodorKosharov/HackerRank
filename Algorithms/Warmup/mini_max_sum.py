nums = list(map(int, input().split()))
nums.sort()

print(f"{sum([x for x in nums[:-1]])} {sum([x for x in nums[1:]])}")
