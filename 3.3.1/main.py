# Philip Birkland, Brandon Howland Calculator
# These are the functions of a calculator
prev_answers = []

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
    return math.pow(x, y)


def square_root(x):
    return math.sqrt(x)


def sin(x):
    return math.sin(x * math.pi / 180)


def cos(x):
    return math.cos(x * math.pi / 180)


def tan(x):
    return math.tan(x * math.pi / 180)


print("what would you like the calculator to do?" + "\n 1. add" + "\n 2. subtract" + "\n 3. multiply" "\n 4. divide" + "\n 5. power" + "\n 6. square root" + "\n 7. Sin" + "\n 8. cos" + "\n 9. tan" + "\n 0. calculation history")

while True:
    choice = input("Choose 1, 2, 3, 4, 5, 6, 7, 8, 9, 0\n")
    try:
        choice = int(choice)
    except ValueError:
        print("input needs to be a number not a letter\n")
    else:
        if choice == 1:
            x = int(input("What are you adding to?"))
            y = int(input("How much are you adding?"))
            print(add(x, y))
            prev_answers.append(str(x) + "+" + str(y) + "=" + str(add(x, y)))

        elif choice == 2:
            x = int(input("What are you subtracting from?"))
            y = int(input("How much are you subtracting by?"))
            print(subtract(x, y))
            prev_answers.append(str(x) + "-" + str(y) + "=" + str(subtract(x, y)))

        elif choice == 3:
            x = int(input("What are you multiplying?"))
            y = int(input("how many times are you multiplying?"))
            print(multiply(x, y))
            prev_answers.append(str(x) + "*" + str(y) + "=" + str(multiply(x, y)))


        elif choice == 4:
            x = int(input("What are you dividing?"))
            y = int(input("how much are you dividing?"))
            print(divide(x, y))
            prev_answers.append(str(x) + "/" + str(y) + "=" + str(divide(x, y)))

        elif choice == 5:
            x = int(input("What number is getting powered?"))
            y = int(input("To what power?"))
            print(power(x, y))
            prev_answers.append(str(x) + "^" + str(y) + "=" + str(power(x, y)))

        elif choice == 6:
            x = int(input("What do you want the square root of?"))
            print(square_root(x))
            prev_answers.append("√" + str(x) + "=" + str(square_root(x)))

        elif choice == 7:
            x = int(input("Sine of what?"))
            print(sin(x))
            prev_answers.append("sin" + str(x) + "=" + str(sin(x)))

        elif choice == 8:
            x = int(input("Cosine of what?"))
            print(cos(x))
            prev_answers.append("cos" + str(x) + "=" + str(cos(x)))

        elif choice == 9:
            x = int(input("Tangent of what?"))
            print(tan(x))
            prev_answers.append("tan" + str(x) + "=" + str(tan(x)))

        elif choice == 0:
            print(prev_answers)