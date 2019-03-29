from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.c4e

rivers = db["river"].find()

for river in rivers:
    if river["continent"] == "Africa":
        print (river)

for river in rivers:
    if river["continent"] == "S. America" and river["length"] < 1000:
        print(river)
