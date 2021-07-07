nums = [1, 2, 4]

print(nums)
print(*nums)


ranges = [*range(5), *"Hello"]
print(ranges)

dick1 = {1: 'x'}
dick2 = {2: 'y'}

dicks = {**dick1, **dick2}
print(dicks)
