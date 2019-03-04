from random import randint
i = randint (0,100)
print (i)
count = 0 
loop = True
while loop:
    n = int(input("Enter a number(0-100): "))
    if count < 3:
        if n < i:
            print ("Lower")
        elif n > i:
            print ("Higher")
        else:
            print ("Bingo")
            loop = False
        count += 1
    else:
        loop = False
        print ("Game over")




