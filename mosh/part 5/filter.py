items = [
    ("num1", 10),
    ("num3", 30),
    ("num2", 20),
]

x = list(filter(lambda item: item[1] > 10, items))
print(x)
