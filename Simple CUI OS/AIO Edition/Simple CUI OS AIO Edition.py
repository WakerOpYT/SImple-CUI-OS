import time

import random as rd

while True:

    print("Welcome To Pubuntu OS. This OS Is Made Using Python")

    app = input("Which App Do You Want To Open? Random Number Game Or OS Info: ")
#    def Typingpad():
#       if app == "Typing pad":
#            type = input("Type 'type' to start typing. Type 'closepro()' to stop typing.")
#            if type == "type":
#                continue
#            elif type == "closepro()":
#                pass

    

    if app == "OS Info":
        if app == "OS Info":
            #f strings:
            print(f"Ram: {ram}")
            print(f"Storage = {storage}")
            print(f"Edition: {edition}")
            print(f"Drives/Partitions: {drives}")
            print(f"OS Drive: {maindrive}")
            print(f"Available for: {availableos}")

            #variables:
            ram = "20 MB"
            storage = "30 MB"
            edition = "All In One Edition"
            drives = "A Drive, C Drive, D Drive, F Drive, H Drive"
            maindrive = "F Drive"
            availableos = "Windows, Mac, Linux, Android & IOS"

    elif app == "Random Number Game":
        if app == "random number game".lower():
            rdnum = rd.randint(1, 10)
            while True:
                rdnumgame = input("Guess The Number(1 To 10): ")
                if rdnumgame == rdnum:
                    print("You Won!")
                
                elif not(rdnumgame.isdigit):
                    print("Bruh Type A Number")

                elif not(rdnumgame == rdnum):
                    print(f"Sorry, The Number Was {rdnum}")


    else:
        print("Bruh Just Choose An App, Random Number Game Or OS Info")