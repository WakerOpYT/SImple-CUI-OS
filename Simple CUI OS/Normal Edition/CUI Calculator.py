while True:

    oper = input("What do you want to do?: ")


    def add():
        print(numadd1 + numadd2)


    def subtract():
        print(numadd1 - numadd2)


    def mutiplication():
        print(numadd1 * numadd2)


    def divide():
        print(numadd1 / numadd2)

    #Inputs:
    if oper == "addition".lower():
        #Input for addition:
        numadd1 = int(input("Enter The First Number:"))#1st number for addition
        numadd2 = int(input("Enter The Second Number")) #2nd number for addition
        add()

    #Input for subtraction:
    if oper == "subtraction".lower():
        numsub1 = int(input("Enter The First Number:")) #1st number for subtraction
        numsub2 = int(input("Enter The Second Number:")) #2nd number for subtraction
        subtract()

    #Input for multiplication:
    if oper == "mulipication".lower():
        nummult1 = int(input("Enter The First Number:")) #1st number for multipication
        nummult2 = input("Enter The Second Number:") #2nd number for mutiplication
        mutiplication()

    #Input for division
    if oper == "division".lower():
        numdiv1 = int(input("Enter The First Number:")) #1st number for division
        numdiv2 = int(input("Enter The Second Number:")) #2nd number for division
        divide()