# n = input ("Enter your yob:")
# age = 2019 - int(n)
# print (age)

# if age < 10:
#     print("Baby")
# if age < 18:
#     print("Teenager")
# else:
#     print("Adult")

from random import randint
# i = randint(3,100)
# print (i)

# x = randint(0,100)
# print (x)
# if x<35:
#     print("Sunny")
# elif x>70:
#     print("Cloudy")
# elif 35<x<70:
#     print("Rainy")

# print ("0=ax^2+bx+c")
# a = int(input("Enter a = "))
# b = int(input("Enter b = "))
# c = int(input("Enter c = "))
# delta = b*b - (4*a*c)

# if delta < 0:
#     print ("Vo nghiem")
# elif delta == 0:
#     print ("Nghiem kep")
# elif delta > 0:
#     print ("2 nghiem")

n = int(input("Enter start number: "))
m = int(input("Enter end number: "))
for i in range (n, m+1):
    if i % 2 == 0:
        print (i)



