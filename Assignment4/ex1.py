# 1 + 2
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
inventory["pocket"] = ["seashell", "strange berry", "lint"]
# 3
choice = inventory["backpack"]
choice.remove("dagger")
# 4
inventory ["gold"] += 50

print (inventory)

