# Jumble game about fruit
import random

print("Welcome to fruit jumble game!!!")
n = input("Press any key to enter")
fruit = ["pineapple", "pomegranate", "strawberry", "star fruit", "mango", "lemon", "avocado"]
print("Let's start!")

print ("You have 5 times")
word = random.choice(fruit)
l = list (word)
random.shuffle(l)
print ()
print (*l, sep= '-')
print ()
loop = True
count = 0
while loop:
    ans = input("Enter your answer: ")
    count += 1
    if ans == word:
        print ("Excellent!!!")
        loop = False
    elif count ==5:
        print("You lose")
        break
    else:
        print ("Try again")
