#7
def remove_dollar_sign(s):
    string = input("Enter a sentence: ")
    new_string = string.replace(s, "")
    return new_string

print (remove_dollar_sign("$"))