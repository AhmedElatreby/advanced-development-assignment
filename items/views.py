import os

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import Blueprint, render_template, request, redirect, url_for
from pymongo import MongoClient

items = Blueprint("items", __name__, template_folder="templates")

# setup fire store
data = os.path.abspath(os.path.dirname(__file__)) + "/serviceAccountKey.json"
cred = credentials.Certificate(data)
firebase_admin.initialize_app(cred)

# connect to fire store db
db = firestore.client()

# create add items route
@items.route("/add_items", methods=["POST", "GET"])
def add_items():
    add_item = request.form.get("add_items")
    print(add_item)
    return render_template("items.html")


# create single page route
@items.route("/items/single/<string:value>")
def get_single(value):
    client = MongoClient(
        "mongodb+srv://ahmed:ahmed@cluster0.wwv1r.mongodb.net/myFirstDatabase?retryWrites=true&w"
        "=majority"
    )
    db = client.item
    collection = db.sofabeds
    sofabed = collection.find_one({"id": value})
    return render_template("single.html", sofabed=sofabed)


# create order summery page route
@items.route("/order_summery/<string:value>", methods=["POST"])
def order_summery(value):
    client = MongoClient(
        "mongodb+srv://ahmed:ahmed@cluster0.wwv1r.mongodb.net/myFirstDatabase?retryWrites=true&w"
        "=majority"
    )
    db = client.item
    collection = db.orders
    sofabed = collection.find_one({})
    print(sofabed)
    return render_template("order_summery.html", products=value)


# create current order page route
@items.route("/create_order/<string:value>", methods=["POST"])
def create_order(value):
    client = MongoClient(
        "mongodb+srv://ahmed:ahmed@cluster0.wwv1r.mongodb.net/myFirstDatabase?retryWrites=true&w"
        "=majority"
    )
    db = client.item
    collection = db.orders
    data = {
        "product_id": value,
        "Type": value,
        "Materia": value,
        "Price": value,
        "Collection": value,
        "Brands": value,
        "Customer rating": value,
    }
    sofabed = collection.insert_one(data)
    print(sofabed)
    return redirect(url_for("items.get_single", value=value))
