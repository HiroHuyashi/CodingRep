def add():
    firstAddend=int(input("Input first addend: "))
    secondAddend=int(input("Input second addend: "))
    print("Result: ", firstAddend+secondAddend)
def subtract():
    minuend=int(input("Input minuend: "))
    subtrahend=int(input("Input subtrahend: "))
    print("Result: ",minuend-subtrahend)
def multiply():
    firstFactor=int(input("Input first factor: "))
    secondFactor=int(input("Input second factor: "))
    print("Result: ",firstFactor*secondFactor)
def divide():
    dividend=int(input("Input dividend: "))
    divisor=int(input("Input divisor: "))
    print("Result: ", dividend/divisor)
def choose(num):
    match num:
        case 1:
            add()
        case 2:
            subtract()
        case 3:
            multiply()
        case 4:
            divide()
        case _:
            print("Choosed wrong option, please try again")
            mainMenu()
def mainMenu():
    print("Main menu:", "1. Add ", "2. Sub ", "3. Multiply ", "4. Div ", sep="\n")
    a=int(input("Choose option: "))
    choose(a)
mainMenu()