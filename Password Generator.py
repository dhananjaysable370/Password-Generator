import random

ps1 = "abcdefghijklmnopqrstuvwxyzABDCEFFGHIKLMNOPQRSTUVWXYZ0123456789!@#$%^&*."

pass_length = int(input("Enter the length of password :"))

pass_num = int(input("Enter the number of passwords you want :"))


for i in range(0, pass_num):
    password = ""
    
    for j in range(0,pass_length):

        pass_char = random.choice(ps1)
        password = password+pass_char
    print("your password is: " +password )

    
