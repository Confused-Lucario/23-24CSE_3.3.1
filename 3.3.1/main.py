# Philip Birkland, Brandon Howland Calculator
# These are the functions of a calculator

import math

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def power(x,y):
    return x^y

def square_root(x):
    return math.sqrt(x)

def sin(x):
    return degrees.sin(x)

def cos(x):
    return degrees.cos(x)

def tan(x):
    return math.tan(x)

print("what would you like the calculator to do?" + "\n 1. add" + "\n 2. subtract" + "\n 3. multiply" "\n 4. divide" + "\n 5. power" + "\n 6. square root" + "\n 7. Sin" + "\n 8. cos" + "\n 9. tan")


choice = int(input("Choose 1, 2, 3, 4, 5 ,6 ,7, 8, 9 \n"))
while type(choice) == int:
    if choice == 1:
        x = int(input("What are you adding to?"))
        y = int(input("How much are you adding?"))
        print(add(x, y))
        choice = int(input("Choose 1, 2, 3, 4, 5 ,6 ,7, 8, 9 \n"))
    elif choice == 2:
        x = int(input("What are you subtracting from?"))
        y = int(input("How much are you subtracting by?"))
        print(subtract(x, y))
        choice = int(input("Choose 1, 2, 3, 4, 5 ,6 ,7, 8, 9 \n"))

    elif choice == 3:
        x = int(input("What are you multiplying?"))
        y = int(input("how many times are you multiplying?"))
        print(multiply(x, y))
        choice = int(input("Choose 1, 2, 3, 4, 5 ,6 ,7, 8, 9 \n"))

    elif choice == 4:
        x = int(input("What are you dividing?"))
        y = int(input("how much are you dividing?"))
        print(divide(x, y))
        choice = int(input("Choose 1, 2, 3, 4, 5 ,6 ,7, 8, 9 \n"))

    elif choice == 5:
        x = int(input("What number is getting powered?"))
        y = int(input("To what power?"))
        print(power(x, y))
        choice = int(input("Choose 1, 2, 3, 4, 5 ,6 ,7, 8, 9 \n"))



    elif choice == 6:
        x = int(input("What do you want the square root of?"))
        print(square_root(x))
        choice = int(input("Choose 1, 2, 3, 4, 5 ,6 ,7, 8, 9 \n"))
    elif choice == 7:
        x = int(input("Sine of what?"))
        print(sin(x))
        choice = int(input("Choose 1, 2, 3, 4, 5 ,6 ,7, 8, 9 \n"))
    elif choice == 8:
        x = int(input("Cosine of what?"))
        print(cos(x))
        choice = int(input("Choose 1, 2, 3, 4, 5 ,6 ,7, 8, 9 \n"))

    elif choice == 9:
        x = int(input("Tangent of what?"))
        print(tan(x))
        choice = int(input("Choose 1, 2, 3, 4, 5 ,6 ,7, 8, 9 \n"))


    elif type(choice) != int:
        print ("invalid choice")
        choice = int(input("choose 1, 2, 3, 4, 5 ,6 ,7, 8, 9"))

        
