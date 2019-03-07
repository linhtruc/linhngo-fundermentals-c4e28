prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stocks = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
for key in stocks.keys():
    print(key)
print ()
while True:
    n = input("Enter key:  ")
    p1 = prices[n]
    s1 = stocks[n]
    print (n)
    print ("prices:",p1)
    print ("stocks:",s1)
    q = (input("Do you want to continue? (Y/N)")).lower()
    if q == "n":
        break
    elif q == "y":
        print()
    else:
        print ("Please try again!")