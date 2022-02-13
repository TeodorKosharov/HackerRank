n, x = map(int, input().split())

res = []
for _ in range(x):
    res.append(list(map(float, input().split())))

res = list(zip(*res))

print('\n'.join([f'{sum(z) / len(z):.2f}' for z in res]))
