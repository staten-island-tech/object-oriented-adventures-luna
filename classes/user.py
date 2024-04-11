import json
import os

class user():
    def __init__(self, username, password, type):
        self.username = username
        self.password = password
        self.type = type

class player(user):
    def __init__(self, username, password, type, version, team_lvl, crystals, stars, character):
        super().__init__(username, password, type)
        self.version = version
        self.team_lvl = team_lvl
        self.crystals = crystals
        self.stars = stars
        self.character = character

class admin(user):
    def __init__(self, username, password, type, rank):
        super().__init__(username, password, type)
        self.rank = rank


with open("user.json", "r") as f:
    data = json.load(f)

    def add():
        a = input("Would you like to add a new user? Y/N").lower()
        while a != "y" or a != "n":
            a = input("Would you like to add a new user? Y/N").lower()
        while a == "y":
            type = input("What type of user would you like to make? (player or admin)").lower()
            while type != "player" or type != "admin":
                type = input("What type of user would you like to make? (player or admin)").lower()
            while type == "player":
                username = input("Choose a username: ")
                users = open("./users.json", encoding="utf8")
                user_data = json.load(users)
                for user in user_data:
                    while username == user["username"]:
                        username = input("Choose another username: ")
                password = input("Choose a password: ")
                version = 0000000000
                team_lvl = 1
                crystals = 0
                characters = []
                stars = 0
                player_made = player(username, password, type, version, team_lvl, crystals, stars, characters)
                print(player_made.__dict__)
                data.append(player_made.__dict__)
            while type == "admin":
                username = "admin_"+ input("Enter your name: ").lower()
                print (username)
                password = input("Enter your password: ")
                rank = 1
                admin_made = admin(username, password, type, rank)
                print(admin_made.__dict__)
                data.append(admin_made.__dict__)





new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps(data)

    # Write the JSON string to the new JSON file
    f.write(json_string)

# Overwrite the old JSON file with the new one
os.remove("user.json")
os.rename(new_file, "user.json")