n, k = map(int, input().split())
cloulds = list(map(int, input().split()))

energy = 100
index = 0

while True:
    jumps = k

    while jumps > 0:  # Calculating the next index we will jump at
        index += 1
        jumps -= 1

        if index == len(cloulds):
            index = 0

    if cloulds[index] == 0:  # Calculating the spent energy depending on which clould we have arrived
        energy -= 1
    else:
        energy -= 3

    if index == 0:  # If after the last jump we are at the beginning (index 0) we break the loop and print the remaining energy
        break

print(energy)
