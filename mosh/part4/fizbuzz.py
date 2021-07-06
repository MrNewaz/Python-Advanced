def fizz_buzz(input):
    if input % 3 != 0 and input % 5 != 0:
        return input
    elif input % 3 == 0 and input % 5 == 0:
        return "fizzbuzz"
    elif input % 3 == 0:
        return "fizz"

    elif input % 5 == 0:
        return "buzz"


print(fizz_buzz(7))
