loop = True
while loop:

    n = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    items = ["T-shirt", "Sweater"]

    if n == ("r"):
        print ("Our items: ", *items)

    elif n == ("c"):
        items = ["T-shirt", "Sweater"]
        m = input("Enter new item: ")
        items.append(m)
        print ("Our items: ", *items)
        
    elif n == ("u"):
        upposition = int(input("Enter update position: "))
        o = input("Enter new item: ")
        items [position-1] = o
        print ("Our items: ", *items)

    elif n == ("d"):
        delposition = int(input("Enter delete position: "))
        del items [delposition-1]
        print ("Our items: ", *items)

    else:
        print ("Try again, please!")
