from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb://localhost:27017/")
db = client["app_database"]
collection = db["users"]

# Converting MongoDB ObjectId attribute to string
def serialize_user(user):
    user["_id"] = str(user["_id"])
    return user


@app.route("/users", methods=["GET"])
def get_users():
    users = list(collection.find())
    return jsonify([serialize_user(user) for user in users])


@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    try:
        user = collection.find_one({"_id": ObjectId(user_id)})
        return jsonify(serialize_user(user))
    except:
        return ("User not found", 404)


if __name__ == "__main__":
    app.run(debug=True)
