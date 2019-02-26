# r1 = range (10)
# print (*r1)

# r2 = range (5, 10)
# print (*r2)

# r3 = range (5, 30, 4)
# print (*r3)

# first number is start
# second number is stop
# third numer is step

# a = range (3+1, 100, 2)
# print (*a)

# b = range (100, 5, -1)
# print (*b)

# c = range (1000, 100,-5)


# for i in [0,1,2,89]:
#     print("Hello")

# for k in range ['f', 'g']:
# print (k)

# total = 0
# for h in range (1,11):
#     total = total + h
# print (total)

# a = range (1,11)
# c = sum(a)
# b = sum([3,4,5])
# print (c)
# print (b)

# a = range (1,11)
# b = sqr(a)

# from turtle import *
# speed(0)
# for j in range (10):
#   forward (5)
#   left (90)
# mainloop ()

from turtle import *

# for i in range (100):
#     forward (10*i)
#     left (90)
# mainloop()
i = 50
for i in range (0,i,i):
    forward (i)
    left (90)
mainloop()