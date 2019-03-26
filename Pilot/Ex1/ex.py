from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.c4e

posts = db["posts"]

new_post = {
    "title": "test",
    "author": "just a test",
    "content": "nothing",
}

posts.insert_one(new_post)