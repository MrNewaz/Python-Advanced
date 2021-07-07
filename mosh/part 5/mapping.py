items = [
    ("num1", 10),
    ("num3", 30),
    ("num2", 20),
]

# prices = []

# for item in items:
#     prices.append(item[1])

prices = list(map(lambda item: item[1], items))

print(prices)
