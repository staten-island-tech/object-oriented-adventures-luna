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

with open (r"game_files/classes/json/users.json", "r") as hi : 
    users = json.load(hi)


class create():
    def add():
        a = input("Would you like to add a new user? y/n ").lower()
        while a != "y" and a != "n":
            a = input("Would you like to add a new user? y/n ").lower()
        while a == "y":
            type = "player"
            if type == "player":
                username = input("Choose a username: ")
                for user in users:
                    # checks for duplicates
                    while username == user["username"]:
                        username = input("Username taken, choose another username: ")
                print(username)
                password = input("Choose a password: ")
                print("Pick your first character: ")
                print("[A] Aelius")
                print("[B] Amaris")
                a = input("").upper()
                b = ["A", "B"]
                while a not in b:
                    print('That is not a character you could choose, please try again.')
                    a = input("").upper()
                if a == b[0]:
                    characters = ["Aelius", "Asahi"]
                    team = ["Aelius","Asahi","",""]
                elif a == b[1]:
                    characters = ["Amaris", "Asahi"]
                    team = ["Amaris","Asahi","",""]
                crystals = 12800
                quest = []
                stars = 0
                player_made = player(username, password, type, crystals, stars, characters, team, quest)
                users.append(player_made.__dict__)
                new_file = "updated.json"
                with open(new_file, "w") as f:
                    json_string = json.dumps(users)
                    f.write(json_string)
                os.remove(r"game_files/classes/json/users.json")
                os.rename(new_file, r"game_files/classes/json/users.json")
            a = "n"
        while a == "n":
            return "thank you for your time."
        

create.add()