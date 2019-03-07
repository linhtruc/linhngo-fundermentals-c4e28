#1

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
# 2
# while True:
#     n = input("Enter key: ")
#     if n in prices:
#         p1 = prices[n]
#         s1 = stocks[n]
#         print (n)
#         print ("prices:",p1)
#         print ("stocks:",s1)
#     else:
#         print ("Please try agian!")

# 3
total = 0
for i in prices:
    total = prices[i]*prices[i]+total
print (total)

