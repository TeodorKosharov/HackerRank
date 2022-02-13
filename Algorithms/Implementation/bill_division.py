n, k = map(int, input().split())
bill = list(map(int, input().split()))
charged_price = int(input())

bill.pop(k)
half_price = sum(bill) / 2

if half_price == charged_price:
    print('Bon Appetit')
else:
    print(abs(int(charged_price - half_price)))
