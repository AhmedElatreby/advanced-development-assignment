from flask import Blueprint, render_template, request, url_for, redirect, session
from pymongo import MongoClient
from pyrebase import pyrebase

navigation = Blueprint("navigation", __name__, template_folder="templates")

# firebase configurations
firebaseConfig = {
    "apiKey": "AIzaSyCaw3xr2fl9kpMCaTR3Jj04XXPjc7BTdNw",
    "authDomain": "adauth-18a13.firebaseapp.com",
    "databaseURL": "https://adauth-18a13-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "adauth-18a13",
    "storageBucket": "adauth-18a13.appspot.com",
    "messagingSenderId": "769245706383",
    "appId": "1:769245706383:web:0f8d1ae414ab6b8555d8fa",
    "measurementId": "${config.measurementId}",
}

# Initialize Firestore DB
firebase = pyrebase.initialize_app(firebaseConfig)
database = firebase.database()


# create form route
@navigation.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        client = MongoClient(
            "mongodb+srv://ahmed:ahmed@cluster0.wwv1r.mongodb.net/myFirstDatabase?retryWrites=true&w"
            "=majority",
            uuidRepresentation="standard",
        )
        db = client.people
        collection = db.user
        user1 = {
            "_id": session["user"]["users"][0]["localId"],
            "first_name": request.form.get("f_name"),
            "last_name": request.form.get("l_name"),
            "email": request.form.get("email"),
            "inputAddress": request.form.get("address1"),
            "inputAddress2": request.form.get("address2"),
            "inputCity": request.form.get("city"),
        }
        users = collection.insert_one(user1)
        return redirect(url_for("navigation.profile"))
    return render_template("form.html")


# create profile route
@navigation.route("/profile")
def profile():
    client = MongoClient(
        "mongodb+srv://ahmed:ahmed@cluster0.wwv1r.mongodb.net/myFirstDatabase?retryWrites=true&w"
        "=majority"
    )
    db = client.people
    collection = db.user
    collection1 = db.sofabeds
    user_id = session["user"]["users"][0]["localId"]
    profile = collection.find_one({"_id": user_id})
    ids = database.child("orders").child(user_id).get().val()
    item = collection1.find_one({})
    orders = []
    if ids:
        for order in ids:
            orders.append(
                database.child("orders").child(user_id).child(order).get().val()
            )
    return render_template("profile.html", profile=profile, orders=orders, item=item)


# connect to mongodb database
@navigation.route("/", methods=["GET"])
def home():
    client = MongoClient(
        "mongodb+srv://ahmed:ahmed@cluster0.wwv1r.mongodb.net/myFirstDatabase?retryWrites=true&w"
        "=majority"
    )
    db = client.item
    collection = db.sofabeds
    products = collection.find({})
    return render_template("home.html", products=products)


# create about route
@navigation.route("/about")
def about():
    return render_template("about.html")


# create 404 route
@navigation.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404
