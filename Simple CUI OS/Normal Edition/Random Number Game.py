import random as rd

def randnumgame():
    rdnum = rd.randint(1, 10)
    while True:
        rdnumgame = input("Guess The Number(1 To 10): ")
        if rdnumgame == rdnum:
            print("You Won!")
           
        elif not(rdnumgame.isdigit):
                print("Bruh Type A Number")

        elif not(rdnumgame == rdnum):
            print(f"Sorry, The Number Was {rdnum}. Try Again!")