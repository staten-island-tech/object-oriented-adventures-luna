import json
import os


class user():
    def __init__(self, username, password, type):
        self.username = username
        self.passward = password
        self.type = type


class player(user):
    def __init__(self, username, password, type, version, team_lvl, crystals, stars):
        super().__init__(username, password, type)
        self.version = version
        self.team_lvl = team_lvl
        self.crystals = crystals
        self.stars = stars

class admin(user):
    def __init__(self, username, password, type, rank):
        super().__init__(username, password, type)
        self.rank = rank

with open("users.json", "r") as f:
    users = json.load(f)
    
    def add_user(username, password, type):
        new_user = user(username, password, type)
        users.append(new_user.__dict__)

    continue_add = "Y"
    while continue_add == "Y":
        user_request = input("What type of user? player or admin ").upper()
        if user_request == "PLAYER":
            username = input("enter username: ")
            password = input("enter password: ")
            type = "PLAYER"
            add_user(username, password)
        if user_request == "ADMIN":

        
        add_user(username, password, type)
        continue_add = input("want to add another user? Y/N ").upper()



new_file = "updated.json"
with open(new_file, "w") as f:
    json_string = json.dumps(users)
    f.write(json_string)

os.remove("users.json")
os.rename(new_file, "users.json")