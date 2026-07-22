import random
import string

length = int(input("Enter password length: "))

chars = string.ascii_letters + string.digits

password = ""

for i in range(length):
    password += random.choice(chars)

password = list(password)
random.shuffle(password)
password = "".join(password)

print("Password:", password)
