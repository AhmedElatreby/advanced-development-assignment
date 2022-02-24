import pyrebase

from flask import Blueprint, redirect, render_template, request, url_for, flash, session
from google.auth.transport import requests

login = Blueprint("login", __name__, template_folder="templates")

# firebase configurations
firebaseConfig = {
    "apiKey": "AIzaSyCaw3xr2fl9kpMCaTR3Jj04XXPjc7BTdNw",
    "authDomain": "adauth-18a13.firebaseapp.com",
    "projectId": "adauth-18a13",
    "storageBucket": "adauth-18a13.appspot.com",
    "messagingSenderId": "769245706383",
    "appId": "1:769245706383:web:0f8d1ae414ab6b8555d8fa",
    "measurementId": "G-8KGWFV8NEH",
    "databaseURL": "https://ad-project-328808-default-rtdb.europe-west1.firebasedatabase.app/",
}
# Initialize Firestore DB
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


# create login page route
@login.route("/login", methods=["GET", "POST"])
def login_page():
    if request.method == "POST":
        session["email"] = request.form.get("email")
        print(session)
        email = request.form["user_email"]
        password = request.form["user_pwd"]
        try:
            user_info = auth.sign_in_with_email_and_password(email, password)
            account_info = auth.get_account_info(user_info["idToken"])
            session["user"] = account_info
            return redirect(url_for("navigation.home"))
        except:
            unsuccessful = "Please check your credentials"
            flash(unsuccessful)
            return render_template("register.html")
    return render_template("login.html")


# create logout route
@login.route("/logout")
def logout():
    session["user"] = None
    return redirect(url_for("navigation.home"))


# create register route
@login.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        pwd0 = request.form.get("user_pwd0")
        pwd1 = request.form.get("user_pwd1")
        if pwd0 == pwd1:
            try:
                email = request.form.get("user_email")
                password = request.form.get("user_pwd1")
                new_user = auth.create_user_with_email_and_password(email, password)
                auth.send_email_verification(new_user["idToken"])
                return render_template("verify_email.html")
            except:
                flash("That account already exists")
                return render_template("register.html")
    return render_template("register.html")


# create reset password route
@login.route("/reset_password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        email = request.form.get("user_email")
        auth.send_password_reset_email(email)
        return render_template("order.html")
    return render_template("reset_password.html")


# create verify_email route
@login.route("/verify_email")
def verify_email():
    return render_template("verify_email.html")


# create submit  route
@login.route("/submitted", methods=["POST"])
def submitted_form():
    url = "https://europe-west2-ad-project-328808.cloudfunctions.net/submitted_form"
    response = requests.get(url)
    return response.content


# create context processor session for user login page
@login.app_context_processor
def current_user():
    if "user" not in session:
        session["user"] = None
    return dict(current_user=session["user"])
