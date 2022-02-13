import collections

products = collections.OrderedDict()

for data in range(int(input())):
    product_data = input().split()
    current_product = ' '.join([x for x in product_data if x.isalpha()])
    current_price = int(*[y for y in product_data if y.isdigit()])

    if current_product not in products:
        products[current_product] = current_price
    else:
        products[current_product] += current_price

for k, v in products.items():
    print(k, v)
