import random
import string

source = string.ascii_letters + string.digits + "!@#$%^&*"


def password_generator(length):
    if length < 6:
        print(
            "Warning: Password length should be at least 6 characters for better security."
        )
        return ""

    return "".join(random.choice(source) for _ in range(length))


pass_length = int(input("Enter the length of each password: "))
pass_num = int(input("Enter the number of passwords you want: "))

for _ in range(pass_num):
    password = password_generator(pass_length)
    if password:
        print("Your password is:", password)
