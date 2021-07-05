successful = False

for item in range(5):
    print('Attempt')
    if successful:
        print('successful')
        break
else:
    print('Failed')
