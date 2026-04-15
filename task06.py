emails = ["ali@gmail.com", "vali@yahoo.com", "sami@gmail.com", "bek@outlook.com"]

result = filter(lambda email: email.endswith("@gmail.com"), emails)
print(list(result))