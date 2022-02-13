def a_very_big_sum(ar):
    return sum(ar)


n = int(input())
arr = [int(x) for x in input().split()]
print(a_very_big_sum(arr))
