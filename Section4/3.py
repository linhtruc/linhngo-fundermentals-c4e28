
print ('''
Think a number from 0  to 101
All you have to do is answer to my guess
Press 'c' if answer correct
Press 's' if your number smaller
Press 'l' if your number larger
''')
low = 1
high = 101
while True:
    mid = (low + high) // 2

    key = input(print ("Is {0} your number?".format(mid)))

    if key == "c":
        print ("I knew it")
        break
        
    elif key == "l":
        high = mid

    elif key == "s":
        low = mid
    
    

