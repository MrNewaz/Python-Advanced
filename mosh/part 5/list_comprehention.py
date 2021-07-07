items = [
    ("num1", 10),
    ("num3", 30),
    ("num2", 20),
]

mapping = [item[1] for item in items]
print(mapping)

filtering = [item for item in items if item[1] > 10]
print(filtering)
