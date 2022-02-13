n = int(input())
candes = list(map(int, input().split()))

print(candes.count(max(candes)))
