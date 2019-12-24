print("The GREATER One :D")
while True:
    numberone = float(input("Enter your first number: "))
    numbertwo = float(input("Enter your second number: "))
    numberthree = float(input("Enter your third number: "))
    if numberone >= numbertwo and numberone >= numberthree:
        print(numberone)
    elif numbertwo > numberone and numbertwo >= numberthree:
        print(numbertwo)
    elif numberthree > numberone and numberthree > numbertwo:
        print(numberthree)
    pass
