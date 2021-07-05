with open('email.txt', 'r') as file:
    emails = file.readlines()

for email in emails:
    # print("Looking for a Hotmail")
    if "hotmail" in email:
        print(email.rstrip())
