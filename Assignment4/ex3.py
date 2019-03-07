while True:
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
        print ("You're right!")
        break
    else:
        print()
        print("Please try again!")

