n, m = [int(x) for x in input().split()]
stations_locations = [int(x) for x in input().split()]

results = []
for city in range(n):
    if city in stations_locations:
        results.append(0)
    else:
        results.append(min([abs(city - x) for x in stations_locations]))

print(max(results))
