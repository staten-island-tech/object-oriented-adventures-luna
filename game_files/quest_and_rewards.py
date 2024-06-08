import json
import os
from rand import *

data_users = open("./game_files/classes/json/users.json", encoding="utf8")
users = json.load(data_users)

data_entities = open("./game_files/classes/json/entities.json", encoding="utf8")
entities = json.load(data_entities)

class quests():                                             #the whole class needs to be tested
    
    def rewards(x, username):           # x is type of mission
        if x == "world":
            rewards = 80
        else:
            rewards = 10
        for user in users:
            if user['username'] == username:
                crystals = user['crystals']
                add = crystals + rewards
                print(f"{username} now has {add} crystals")
                user['crystals'] = add
        new_file = "updated.json"
        with open(new_file, "w") as f:
            json_string = json.dumps(users)
            f.write(json_string)
        os.remove(r"game_files\classes\json\users.json")
        os.rename(new_file, r"game_files\classes\json\users.json") 
    def lose(username, team):
        a = 0
        for character in team:
            if character['hp'] == 0:
                a += 1
        if a == 4:
            print(f"{username}, you have lost this battle. You will now be transported back to the spaceship for further treatment.")
    def win(enemies, username, quest):
        a = []
        c = []
        for enemy in enemies:
            a.append(enemy['hp'])
        if sum(a) == 0:
            print(f"{username}, you have passed this hurdle. May your journey be rich in prosperity and sopistication.")
            for user in users:
                if user['username'] == username:
                    c = user['quest']
                    c.append(quest)
            new_file = "updated.json"
            with open(new_file, "w") as f:
                json_string = json.dumps(users)
                f.write(json_string)
            os.remove(r"game_files\classes\json\users.json")
            os.rename(new_file, r"game_files\classes\json\users.json")
    def wave(x, e):   # x = wave number(current) z = world(taiyo, etc)
        a = int(x)
        if e == 0:
            print(f"Wave {a+1}: Normal Battle")
        else:
            print(f"Wave {a+1}: Boss Battle")

"""     def enemy(x, username):
        if x == "monde":
            enemy = ["Hydro Robot", "Hydro Robot Dog", "Giant Hydro Robot"]
        elif x == "pero":
            enemy = ["Oblivion Gaurds", "Ice Goblin", "Ice Archer Goblin", "Yeti"]
        elif x == "taiyo":
            enemy = ["Trainee Guard", "Guard", "Guard Captain", "Queen of Taiyo"]
        elif x == "spaceship":
            enemy = ["Oblivion Guard", "Oblivion Drone", "General Aeron"]
        elif x == "choose":
            print("Please note that you could only choose the worlds you have already passed.")
            completed = []
            for user in users:
                if user['username'] == username:
                    completed = user['quest']
            y = input("Choose a world: ").lower()
            if y not in completed:
                pass                                # import error timetraveller
            if y == "monde":
                enemy = ["Hydro Robot"]
            elif y == "pero":
                enemy = ["Oblivion Guard", "Ice Goblin"]
            elif y == "taiyo":
                enemy = ["Trainee Guard"]
            elif y == "spaceship":
                pass """
