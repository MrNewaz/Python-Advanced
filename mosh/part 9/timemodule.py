import time


def send_emails():
    for i in range(10000):
        print(time.time())


send_emails()
