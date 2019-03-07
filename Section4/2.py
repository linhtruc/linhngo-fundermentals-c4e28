user = "c4e"
pw = "codethechange"
count1 = 0
n = input ("Enter username: ")
while True:
    count1 += 1
    if n == user:
        m = input ("Enter password: ")
        count = 0
        while True:
            count += 1
            if m == pw:
                print ("Welcome!")
                break
            elif count == 3:
                break
            else:
                print ("Try again, please!")
    elif count1 == 3:
        break
    else:
        print ("Not found")