# numbers = [1, 23, 5, 14, 23]
# print(sorted(numbers, reverse=True))

# numbers.sort(reverse=True)

# print(numbers)

items = [
    ("num1", 10),
    ("num3", 30),
    ("num2", 20),
]


def sortItems(item):
    return item[1]


items.sort(key=sortItems)
print(items)
