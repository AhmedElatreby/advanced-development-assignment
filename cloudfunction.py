from bson.json_util import dumps
from pymongo import MongoClient


# get staff list function
def get_staff_list(request):
    # mongodb connection link
    client = MongoClient(
        "mongodb+srv://ahmed:ahmed@cluster0.wwv1r.mongodb.net/myFirstDatabase?retryWrites=true&w"
        "=majority"
    )

    # to connect to db
    db = client.people

    # connect to staff collection
    staff = db.staff

    # list staff name with first name = Robbie
    myCursor = staff.find({"first_name": "Robbie"})
    list_cur = list(myCursor)
    print("List of staff who first name is Robbie: ", list(list_cur))
    print("------------")

    # to count number of db in staff collection
    print("Number of users: ", staff.count_documents({}))
    print("-----------")
    json_data = dumps(list_cur)
    return json_data


# display_media_units function
#  https://europe-west2-ad-project-328808.cloudfunctions.net/display_media_units


def get_mediaunits_list(request):
    client = MongoClient(
        "mongodb+srv://ahmed:ahmed@cluster0.wwv1r.mongodb.net/myFirstDatabase?retryWrites=true&w"
        "=majority"
    )

    db = client.item
    mediaunits = db.mediaunits

    myCursor = db.mediaunits.find({}).limit(3)
    list_cur = list(myCursor)
    print(list_cur)

    json_data = dumps(list_cur)

    return json_data


# get a list of staff function
# https://europe-west2-ad-project-328808.cloudfunctions.net/staff_list-1
def get_staff_list(request):
    client = MongoClient(
        "mongodb+srv://ahmed:ahmed@cluster0.wwv1r.mongodb.net/myFirstDatabase?retryWrites=true&w"
        "=majority"
    )

    # to connect to db
    db = client.people

    # connect to staff collection
    staff = db.staff

    # list staff name with first name = Robbie
    myCursor = staff.find({"first_name": "Robbie"})
    list_cur = list(myCursor)
    print("List of staff who first name is Robbie: ", list(list_cur))
    print("------------")

    # to count number of db in staff collection
    print("Number of users: ", staff.count_documents({}))
    print("-----------")
    json_data = dumps(list_cur)
    return json_data


# get list sofa mongodb
# https://europe-west2-ad-project-328808.cloudfunctions.net/get_sofa_mongodb


def get_sofa_mongodb(request):
    client = MongoClient(
        "mongodb+srv://ahmed:ahmed@cluster0.wwv1r.mongodb.net/myFirstDatabase?retryWrites=true&w"
        "=majority"
    )

    db = client.item
    sofa = db.sofa

    myCursor = db.sofa.find({}).limit(3)
    list_cur = list(myCursor)
    print(list_cur)

    json_data = dumps(list_cur)

    return json_data
