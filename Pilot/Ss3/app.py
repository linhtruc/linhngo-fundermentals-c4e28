from flask import *

from pymongo import MongoClient
from faker import Faker
from random import randint, choice
from bson.objectid import ObjectId


mongo_uri = "mongodb+srv://admin:admin@c4e28-xzlj8.mongodb.net/test?retryWrites=true"
client = MongoClient(mongo_uri)
services_database = client.db_services
bike = services_database["bike"]

app = Flask(__name__)

@app.route('/new_bike', methods=["GET", "POST"])
def new_bike():
    if request.method == "GET":
        return render_template("bike.html")
    elif request.method == "POST":
        form = request.form
        model = form["model"]
        fee = form["fee"]
        image = form["image"]
        year = form["year"]
        new_value = {
            "model": model,
            "fee": fee,
            "image": image,
            "year": year,
        }
        bike.insert_one(new_value)
        return redirect('/new_bike')

if __name__ == '__main__':
    app.run(debug=True)
 