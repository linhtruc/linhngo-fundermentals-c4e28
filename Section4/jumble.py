from random import choice

w = ["jellyfish", "champion"]
word = choice(w)
random_list = []
l = list(word)

while len(l) > 0:
    char = choice(l)
    random_list.append(char)
    l.remove(char)
print (*random_list, sep="-")

loop = True
while loop:
    answer = input("Your answer: ")
    if answer == word:
        print ("Hura!")
        break
    else:
        print (":'((")