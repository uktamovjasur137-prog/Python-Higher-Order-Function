votes = [
  {"option": "A", "votes": 123},
  {"option": "B", "votes": 145},
  {"option": "C", "votes": 97}
]

result = max(votes, key=lambda vote: vote["votes"])
print(result)  