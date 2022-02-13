nums = []

for _ in range(int(input())):
    nums.append(input())

for el in sorted(nums, key=int):
    print(el)
