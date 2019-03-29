from pymongo import MongoClient

import matplotlib.pyplot as plt

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.c4e

customers = db["customers"].find()


events = 0
ads = 0
wom = 0

for customer in customers:
    if customer["ref"] == "events":
        events +=1
    elif customer["ref"] == "ads":
        ads +=1
    else:
        wom +=1

print ("Events: ", events)
print ("Advertisements:", ads)
print ("word of mouth:", wom)

labels = ["Events", "Advertisements", "Word of mouth"]
count = int(events), int(ads), int(wom)
colors = ["Turquoise", "Salmon", "DarkOrange"]
plt.title("References")
plt.pie (count, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True)
plt.show()







