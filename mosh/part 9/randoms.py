import random
import string

print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 34]))
print(random.choices([1, 2, 34], k=2))
print("".join(random.choices(string.ascii_letters+string.digits, k=6)))

number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(number)
print(number)
