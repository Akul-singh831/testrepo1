dict={"heera":1234,"moti":5678,"sheela":1298}

def check():
    try:
        name = input("Enter the name you want to search : ")
        print(dict[name])
    except KeyError:
        print("Contact not found")

def enter_new():
    name = input("Enter the new name : ")
    contact = int(input("Enter the new contact : "))
    dict[name] = contact

check()
enter_new()
check()
