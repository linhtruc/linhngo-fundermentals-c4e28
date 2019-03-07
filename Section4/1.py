#1
n = int(input("Enter a number: "))

is_prime = True
i = 2 #2
if n == 0 or n == 1:
    is_prime = False
    print (n, "isn't  prime number")
else:
    while i<n: #2
    #1 for i in range (2,n):
        if n %i == 0:
            is_prime = False
            print (n, "isn't  prime number")
            break
        i += 1 #2
    if is_prime == True:
        print (n, "is  prime number")
    

    

