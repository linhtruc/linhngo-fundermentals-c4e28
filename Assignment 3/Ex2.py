
sheep = [12, 34, 68, 478, 723, 98, 34, 87, 406, 279, 29, 1, 4, 8]
#1
print ("Hello, I'm Moon Jellyfish!")
print ("There are my sheep sizes: ")
print (*sheep, sep=", ")

#2
print ("My biggest sheep size: ",max(sheep))

#3
position = sheep.index(max(sheep))
print ("Bigest is: ", sheep[position])
print ("Biggest size replace by 8, new sheep sizes: ")
sheep [position] = 8
print (*sheep, sep=", ")

#4
print()
print ("MONTH 1:")
for item in sheep:
    item = item + 50
    print (item, end=', ')

print ()
print ("Biggest is: ", sheep[position])
print ("Biggest size replace by 8, new sheep sizes: ")
position = sheep.index(max(sheep))
sheep[position] = 8
print (*sheep, sep=", ")

#6
print ()
print ("MONTH 2:")
for item in sheep:
    item = item + 100
    print (item, end=', ')

print ()
print ("Biggest is: ", sheep[position])
print ("Biggest size replace by 8, new sheep sizes: ")
position = sheep.index(max(sheep))
sheep[position] = 8
print (*sheep, sep=", ")

print ()
print ("MONTH 3:")
for item in sheep:
    item = item + 150
    print (item, end=', ')
    
print ()
print ("Biggest is: ", sheep[position])
print ("Biggest size replace by 8, new sheep sizes: ")
position = sheep.index(max(sheep))
sheep[position] = 8
print (*sheep, sep=", ")

#5
total = sum(sheep)
print ("I would have:", total, "* 2$ = ", total * 2, "$")


