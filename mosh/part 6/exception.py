try:
    with open('./exceptions.py') as fine, open('another.txt'):
        print('Hmmm')
    age = int(input('De? '))

except (ValueError, ZeroDivisionError)as ex:

    print(ex)
else:
    print('Error dey nai')
