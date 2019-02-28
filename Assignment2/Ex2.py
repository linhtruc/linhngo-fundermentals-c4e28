#Calculate n!

n = int(input("Enter a number: "))
result = 1
for i in range (n):
    result = result * (i+1)
print (n,"!=",result)