nums = list(range(1, 21))

result = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, nums))
print(list(result))