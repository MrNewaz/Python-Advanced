def number(*num):
    total = 1
    for n in num:
        total *= n
    return total


print(number(1, 2, 3, 4, 5))
