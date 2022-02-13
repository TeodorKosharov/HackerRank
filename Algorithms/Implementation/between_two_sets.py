import math

x, y = input().split()
first_arr = list(map(int, input().split()))
second_arr = list(map(int, input().split()))

lcm = math.lcm(*first_arr)
gcd = math.gcd(*second_arr)

print(sum(1 for x in range(lcm, gcd + 1, lcm) if gcd % x == 0))
