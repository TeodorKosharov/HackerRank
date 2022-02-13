# Home position coordinates:
x, y = list(map(int, input().split()))  # x - starting point;   y = end point

# Trees positions:
a, o = list(map(int, input().split()))  # a = apple tree position;   o - orange tree position

# 'm' apples and 'n' oranges:
m, n = list(map(int, input().split()))

# Distances each apple falls from point 'a':
apple_fall_distances = list(map(int, input().split()))

# Distances each orange falls from point 'o':
orange_fall_distances = list(map(int, input().split()))

# Finding the count of fallen apples in the home position:

# First variant:

# apples = 0
# for fallen_apple_position in apple_fall_distances:
#     if x <= fallen_apple_position + a <= y:
#         apples += 1
#
# print(apples)
#
# # Finding the count of fallen oranges in the home position:
# oranges = 0
# for fallen_orange_position in orange_fall_distances:
#     if x <= fallen_orange_position + o <= y:
#         oranges += 1
#
# print(oranges)

# Second variant:

print(len([z for z in apple_fall_distances if x <= z + a <= y]))
print(len([z for z in orange_fall_distances if x <= z + o <= y]))
