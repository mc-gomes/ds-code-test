import json
from pymongo import MongoClient
from models import User, UserPreferences

# Creating and conecting to the database
client = MongoClient("mongodb://localhost:27017")
db = client["app_database"]
collection = db["users"]


# Mapping different user roles
def map_roles(user_data):
    roles = []
    if user_data.get('is_user_admin', False):
        roles.append('admin')
    if user_data.get('is_user_manager', False):
        roles.append('manager')
    if user_data.get('is_user_tester', False):
        roles.append('tester')

    return roles


def parse_and_insert_data(data):
    for user_data in data['users']:

        roles = map_roles(user_data)
        
        preferences = UserPreferences(timezone=user_data["user_timezone"])

        user = User(
            username=" ".join(user_data["user"].split("_")[:2]).title(),
            password=user_data["password"],
            roles=roles,
            preferences=preferences.timezone,
            active=user_data.get("is_user_active", True),
            created_ts=user_data["created_at"]
        )
        
        collection.insert_one(user.__dict__)

    print("Users imported successfully!")

if __name__ == "__main__":
    # Importing database
    with open("udata.json", 'r') as f:
        data = json.load(f)
    
    parse_and_insert_data(data)

