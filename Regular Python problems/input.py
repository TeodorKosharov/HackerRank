x, k = map(int, input().split())
expression = input()

result_of_expression = eval(expression)
print(True if result_of_expression == k else False)
