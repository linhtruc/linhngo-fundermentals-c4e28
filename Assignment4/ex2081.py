n = input ("Enter a sentence: ")
n = n.lower()
letter_counts = {}
for letter in n:
    letter_counts[letter] = letter_counts.get(letter, 0) + 1
for key, value in letter_counts.items():
    print(key, value)
