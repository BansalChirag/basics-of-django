import requests
import json


URL = "http://localhost:8000/studentapi/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {"id": id}
    json_data = json.dumps(data)
    print(json_data)
    r = requests.get(url=URL, data=json_data)

    data = r.json()
    print("data : ", data)


# get_data(2)


# other way
# import requests

# def get_data():
#     r = requests.get("http://localhost:8000/student_api/?id=1")
#     print("Response text:", r.text)
#     data = r.json()
#     print("Data:", data)

# get_data()


def post_data():
    data = {"name": "John", "roll": 104, "city": "New York"}
    print("data :", data)

    json_data = json.dumps(data)
    print("json_data : ", json_data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print("data : ", data)


# post_data()


def update_data():
    data = {
        "id": 4,
        "name": "Rohit",
    }
    print("data :", data)

    json_data = json.dumps(data)
    print("json_data : ", json_data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print("data : ", data)


# update_data()


def delete_data():
    data = {
        "id": 3,
    }

    json_data = json.dumps(data)

    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print("data : ", data)

delete_data()
