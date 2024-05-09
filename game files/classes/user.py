import json
import os


class user():
    def __init__(self, username, password, type):
        self.username = username
        self.password = password
        self.type = type

class player(user):
    def __init__(self, username, password, type, version, crystals, stars, character):
        super().__init__(username, password, type)
        self.version = version
        self.crystals = crystals
        self.stars = stars
        self.character = character

with open(r"classes/json/users.json", "r") as f:
    data = json.load(f)

    def add():
        a = input("Would you like to add a new user? y/n ").lower()
        while a != "y" and a != "n":
            a = input("Would you like to add a new user? y/n ").lower()
        while a == "y":
            type = input("What type of user would you like to make? (player/admin) ").lower()
            while type != "player" and type != "admin":
                type = input("What type of user would you like to make? (player/admin) ").lower()
            if type == "player":
                username = input("Choose a username: ")
                users = open(r"classes\users.json", encoding="utf8")
                user_data = json.load(users)
                for user in user_data:
                    # checks for duplicates
                    while username == user["username"]:
                        username = input("Username taken, choose another username: ")
                print(username)
                password = input("Choose a password: ")
                version = 0000000000
                crystals = 0
                characters = [] 
                stars = 0
                player_made = player(username, password, type, version, crystals, stars, characters)
                print(player_made.__dict__)
                data.append(player_made.__dict__)
            a = input("Would you like to add a new user?").lower()
        while a == "n":
            return "thank you for your time."
    add()


new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps(data)

    # Write the JSON string to the new JSON file
    f.write(json_string)

# Overwrite the old JSON file with the new one
os.remove(r"classes\users.json")
os.rename(new_file, r"classes\users.json")
