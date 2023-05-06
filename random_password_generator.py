import string
import random

characters = list(string.ascii_letters + string.digits + "%+#&/_'!")
flag = input("Do you want to generate a rondom password? Y or N: ")


def generate_password():
    lenght = int(input("What will be your lenght of the password? "))
    random.shuffle(characters)
    password = []
    for i in range(lenght):
        password.append(random.choice(characters))    
    random.shuffle(password)
    password = "".join(password)
    print(password)

if flag.upper() == "Y":
    generate_password()
elif flag.upper() == "N":
    print("Program ended")
    quit()
else:
    print("Invalid request !")
    quit()



