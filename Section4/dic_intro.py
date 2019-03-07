# key: value

person = {
    "name": "Jellyfish",
    "age": 1,
    "reborn": 8,
    "language": "none"
}

# Read
# name = person["name"]
# print (name)

# for  key in person.keys():
#     print(key)

# for value in person.values():
#     print (value)


# for key, value in person.items():
#     print(key, value)


# Create and update

# person["city"] = "Nha Trang" #New
# person["reborn"] = 3 #Update

# print(person)



# Delete
del person["reborn"]
print(person)

