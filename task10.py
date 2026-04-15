text = ["apple", "34", "banana", "100", "abc", "75"]

def is_digit(x):
    return x.isdigit()

result = filter(is_digit, text)
print(list(result))