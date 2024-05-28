import json
import os

with open (r"game_files\classes\json\users.json", "r") as hi : 
    users = json.load(hi)

with open (r"game_files\classes\json\entities.json", "r") as bye :
    entities = json.load(bye)

class quests():                                             #the whole class needs to be tested
    def rewards(x, username):           # x is type of mission? yep
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
    def lose(username):
        a = 0
        for user in users:
            if user['username'] == username:
                team = user['team']
                print(team)
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
            if user['name'] == username:
                c = user['quest']
                c.append(quest)
        new_file = "updated.json"
        with open(new_file, "w") as f:
            json_string = json.dumps(users)
            f.write(json_string)
        os.remove(r"game_files\classes\json\users.json")
        os.rename(new_file, r"game_files\classes\json\users.json")
    def enemy(x, username):
        if x == "monde":
            enemy = ["Hydro Robot", "Hydro Robot Dog", "Giant Hydro Robot"]
        elif x == "pero":
            enemy = ["Oblivion Gaurds", "Ice Goblin", "Ice Archer Goblin", ""]
        elif x == "taiyo":
            enemy = []
        elif x == "spaceship":
            enemy = []
        elif x == "choose":
            print("Please note that you could only choose the worlds you have already passed.")
            completed = []
            for user in users:
                if user['name'] == username:
                    completed = user['quest']
            y = input("Choose a world: ").lower()
            if y not in completed:
                pass                                # import error timetraveller
            if y == "monde":
                enemy = []
            elif y == "pero":
                enemy = []
            elif y == "taiyo":
                enemy = []
            elif y == "spaceship":
                pass
    def wave(x, y, z):   # x = wave umber(current) y = what type of battle(not current/normal or boss) z = world(taiyo, etc)
        if y <= 2:
            print(f"Wave {x+1}: {y} Battle")
        elif:
            print(f"")
        a = z.lower()
        

quests.lose("ex")
