import uuid

import pyrebase
from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    redirect,
    jsonify,
    session,
)

from flask_pymongo import MongoClient

from db.views import connect_to_sofa_db


order = Blueprint("order", __name__, template_folder="templates")

firebaseConfig = {
    "apiKey": "AIzaSyCaw3xr2fl9kpMCaTR3Jj04XXPjc7BTdNw",
    "authDomain": "adauth-18a13.firebaseapp.com",
    "databaseURL": "https://adauth-18a13-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "adauth-18a13",
    "storageBucket": "adauth-18a13.appspot.com",
    "messagingSenderId": "769245706383",
    "appId": "1:769245706383:web:0f8d1ae414ab6b8555d8fa",
    "measurementId": "G-8KGWFV8NEH",
}
# setup connection to firebase
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()


# add order route with connecting to firebase
@order.route("/order/<string:product>", methods=["GET", "POST"])
def add_order(product):
    data = {"product_id": product, "qty": request.form.get("qty")}
    db.child("orders").child(session["user"]["users"][0]["localId"]).child(
        str(uuid.uuid4())
    ).set(data)
    return redirect(url_for("navigation.profile"))


# connect to mongodb database
def connect_to_sofa_db():
    client = MongoClient(
        "mongodb+srv://ahmed:ahmed@cluster0.wwv1r.mongodb.net/myFirstDatabase?retryWrites=true&w"
        "=majority"
    )
    db = client.item
    sofabeds = db.sofabeds
    return sofabeds


# order item rote
@order.route("/order")
def order_item():
    todo = db.child("data").get()
    to = todo.val()
    print(to)
    return render_template("order.html", items=to.values())


# add order
@order.route("/order/add", methods=["POST"])
def order_add():
    name = request.form.get("name")
    db.child("data").push(name)
    db.child("data").get().val
    return redirect(url_for("order.order_item"))


# delete order
@order.route("/order/delete/<string:ident>")
def order_delete(ident):
    db.child("data").child(ident).remove()
    return redirect(url_for("order.order_item"))


# single page for products
@order.route("/item/single", methods=["GET"])
def get_item():
    db = connect_to_sofa_db()
    results = []
    sofabeds = db.sofabeds

    for s in sofabeds.find({}):
        results.append({"Type": s["type"], "MaterialType": s["material"]})

    myCursor = db.find({})
    list_cur = list(myCursor)

    return jsonify({"output": results})
    return render_template("single.html", sofabeds=list_cur)
