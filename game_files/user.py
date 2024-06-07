import json
import os

class user():
    def __init__(self, username, password, type):
        self.username = username
        self.password = password
        self.type = type

class player(user):
    def __init__(self, username, password, type, crystals, stars, characters, team, quest):
        super().__init__(username, password, type)
        self.crystals = crystals
        self.stars = stars
        self.characters = characters
        self.team = team
        self.quest = quest

with open(r"game_files\classes\json\users.json", "r") as f:
    user_data = json.load(f)

class create():
    def add():
        a = input("Would you like to add a new user? y/n ").lower()
        while a != "y" and a != "n":
            a = input("Would you like to add a new user? y/n ").lower()
        while a == "y":
            type = input("What type of user would you like to make? (player) ").lower()
            while type != "player" and type != "admin":
                type = input("What type of user would you like to make? (player) ").lower()
            if type == "player":
                username = input("Choose a username: ")
                for user in user_data:
                    # checks for duplicates
                    while username == user["username"]:
                        username = input("Username taken, choose another username: ")
                print(username)
                password = input("Choose a password: ")
                crystals = 0
                characters = [] 
                team = ["","","",""]
                quest = []
                stars = 0
                player_made = player(username, password, type, crystals, stars, characters, team, quest)
                print(player_made.__dict__)
                user_data.append(player_made.__dict__)
                new_file = "updated.json"
                with open(new_file, "w") as f:
                    json_string = json.dumps(user_data)
                    f.write(json_string)
                os.remove(r"game_files\classes\json\users.json")
                os.rename(new_file, r"game_files\classes\json\users.json")
            a = "n"
        while a == "n":
            return "thank you for your time."
        
        

#create.add()

