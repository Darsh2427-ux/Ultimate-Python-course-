import random 
import string
from time import sleep

def Password():
    ranges = 12
    password =""
    hash = string.ascii_letters + string.digits + string.punctuation

    for i in range(ranges):
        password += random.choice(''.join(hash))
    print(password)
    sleep(5)
Password()