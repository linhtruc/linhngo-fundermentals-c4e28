# n stars and xs in total
n = int(input("Enter a number: "))
for i in range (n):
    if i %2 ==0:
        print ("x", end=' ')
    else:
        print ("*", end=' ')