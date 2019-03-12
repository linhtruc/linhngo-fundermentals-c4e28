from random import *

x = randint(0,10)
y = randint(0,10)
op = ["+", "-", "*", "/"]
choice = choice(op)
result = 0
error = randint(-1, 1)
display_result = result + error

def generate_quiz(x, y,choice, result):
    # Hint: Return [x, y, op, result]
    if choice == "+":
        result = x + y
        display_result = result + error
        print (x, choice, y, "=", display_result)
    elif choice == "-":
        result = x - y
        display_result = result + error
        print (x, choice, y, "=", display_result)
    elif choice == "*":
        result = x * y
        display_result = result + error
        print (x, choice, y, "=", display_result)
    else:
        result = x / y
        display_result = result + error
        print (x, choice, y, "=", display_result)

    user_choice = input("y/n? ").lower

    if error == 0:
        if user_choice == "y":
            return True
        elif user_choice == "n":
            return False
        
    else:
        if user_choice == "n":
            return True
        elif user_choice == "y":
            return False
    
    return True or False

print (generate_quiz(x, y, choice, result))
# def check_answer(x, y, choice, result, user_choice):