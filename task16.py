data = [123, "apple", "banana", "cat", 456, "mango", "elephant"]

result = filter(lambda x: len(x) <= 5, filter(lambda x: isinstance(x, str), data))
print(list(result))