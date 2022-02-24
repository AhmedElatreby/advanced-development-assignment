from flask import Blueprint, render_template, request, url_for, redirect
from pymongo import MongoClient

db = Blueprint("db", __name__, template_folder="templates")


# create list of products route
@db.route("/sofabed/list", methods=["GET"])
def sofabed_list():
    db = connect_to_sofa_db()
    myCursor = db.find({})
    list_cur = list(myCursor)
    return render_template("data.html", sofabeds=list_cur)


# create list of users route
@db.route("/user/list", methods=["GET"])
def user_list():
    db = connect_to_user_db()
    myCursor = db.find({})
    list_cur = list(myCursor)
    return render_template("data.html", users=list_cur)


# create add products route
@db.route("/sofabed/add", methods=["POST"])
def sofabed_post():
    db = connect_to_sofa_db()
    data = {
        "Type": request.form.get("type"),
        "MaterialType": request.form.get("material"),
    }
    db.insert_one(data)
    return redirect(url_for("db.sofabed_list"))


# create function for user details
@db.route("/user/add", methods=["POST"])
def user_post():
    db = connect_to_user_db()
    data = {
        "first_name": request.form.get("first_name"),
        "last_name": request.form.get("last_name"),
    }
    db.insert_one(data)
    return redirect(url_for("db.user_list"))


# create function to connect to mongodb for user database
def connect_to_user_db():
    client = MongoClient(
        "mongodb+srv://ahmed:ahmed@cluster0.wwv1r.mongodb.net/myFirstDatabase?retryWrites=true&w"
        "=majority"
    )
    db = client.people
    user = db.user
    return user


# create function to connect to mongodb for products database
def connect_to_sofa_db():
    client = MongoClient(
        "mongodb+srv://ahmed:ahmed@cluster0.wwv1r.mongodb.net/myFirstDatabase?retryWrites=true&w"
        "=majority"
    )
    db = client.item
    sofabeds = db.sofabeds
    return sofabeds


# create user add item route
@db.route("/user_add_item", methods=["POST"])
def user_add_item():
    item = request.form.get("add-item")
    print(user_add_item)
    print(item)
    return redirect(url_for("db.list1"))
