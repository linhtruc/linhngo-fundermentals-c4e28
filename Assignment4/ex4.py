loop = True
while loop:
    print('''
Answer the following algebra question:
If x = 8, then the value of 4(x + 3) ?
a. 35
b. 36
c. 40
d. 44
    ''')
    your_choice = input("Your choice: ").lower()
    if your_choice == "d":
        print ("Bingo!")
        loop = False
    else:
        print(":'((")
        loop = False
l = True
while l:
    print('''
Estimate this answer (exact calculation not needed):
Jack scored these mark in 5 test: 49, 81, 66 and 52. What is the mean?
a. About 55
b. About 65
c. About 75
d. About 85
    ''')
    ans = input("Your choice: ").lower()
    if ans == "b":
        print ("Bingo!")
        break
    else:
        print (";'((")
        break