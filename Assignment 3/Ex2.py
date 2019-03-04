
sheep = [12, 34, 68, 478, 723, 98, 34, 87, 406, 279, 29, 1, 4, 8]
#1
print ("Hello, I'm Moon Jellyfish!")
print ("There are my sheep sizes: ")
print (sheep)

#2
print ("My biggest sheep size: ",max(sheep))

#3
position = sheep.index(max(sheep))
print ("Biggest is: ", sheep[position])
print ("Biggest size replace by 8, new sheep sizes: ")
sheep[position] = 8
print (sheep)

#4

for i in range(int(len(sheep))):
    sheep[i] = sheep[i] + 50
print (sheep)

#5
print ()
print ("MONTH 1:")
for i in range(int(len(sheep))):
    sheep[i] = sheep[i] + 50
print (sheep)
print ()
position = sheep.index(max(sheep))
print ("Biggest is: ", sheep[position])
print ("Biggest size replace by 8, new sheep sizes: ")
sheep[position] = 8
print (sheep)

print()
print ("MONTH 2:")
for i in range(int(len(sheep))):
    sheep[i] = sheep[i] + 50
print (sheep)
print ()
position = sheep.index(max(sheep))
print ("Biggest is: ", sheep[position])
print ("Biggest size replace by 8, new sheep sizes: ")
sheep[position] = 8
print (sheep)

print()
print ("MONTH 2:")
for i in range(int(len(sheep))):
    sheep[i] = sheep[i] + 50
print (sheep)
print ()
position = sheep.index(max(sheep))
print ("Biggest is: ", sheep[position])
print ("Biggest size replace by 8, new sheep sizes: ")
sheep[position] = 8
print (sheep)

#6
total = sum(sheep)
print ("I would get", total, "* 2$ = ", total * 2, "$")
