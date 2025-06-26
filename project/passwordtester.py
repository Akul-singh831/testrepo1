user1 = input("Enter username1: ")
pass1 = input("Enter password1: ")
user2 = input("Enter username2: ")
pass2 = input("Enter password2: ")
user3 = input("Enter username3: ")
pass3 = input("Enter password3: ")

usernames = ("Amar", "Akbar", "Anthony")
passwords = ("123", "456", "789") 

if (user1 in usernames and pass1 in passwords):
    print("successful")
else:
    print("failed")

if (user2 in usernames and pass2 in passwords):
    print("successful")
else:
    print("failed")

if (user3 in usernames and pass3 in passwords):
    print("successful")
else:
    print("failed")
