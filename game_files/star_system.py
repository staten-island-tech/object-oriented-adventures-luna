import os
import json
import random

with open (r"game_files\classes\json\users.json", "r") as hi : 
    users = json.load(hi)

with open (r"game_files\classes\json\entities.json", "r") as bye :
    entities = json.load(bye)

char = {
                "name": "Amaris",
                "hp": 0,
                "attack": [
                    500,
                    1500
                ],
                "rarity": "*****",
                "weapon": "stellar gun",
                "type": "destruction",
                "element": "quantum"
            }

class star():
    k = 15

    def view_characters(username):            #tested
        for user in users: 
            if user['username'] == username:
                characters = user['characters']
                print(f"{username} currently has these characters: ")
                for i in characters:
                    print(i)

    
    def check_dupe_or_append(username, char):
        for user in users:
            if user['username'] == username:
                characters = user['characters']
        names = []
        for character in characters:
            names.append(character['name'])
        if char['name'] in names:
            user['crystals'] += 80
            user['stars'] += 1
            new_file = "updated.json"
            with open(new_file, "w") as f:
                json_string = json.dumps(users)
                f.write(json_string)
            os.remove(r"game_files\classes\json\users.json")
            os.rename(new_file, r"game_files\classes\json\users.json")
            os.system("cls")
            return
        else: 
            user['characters'].append(char)
            user['stars'] += 1
            new_file = "updated.json"
            with open(new_file, "w") as f:
                json_string = json.dumps(users)
                f.write(json_string)
            os.remove(r"game_files\classes\json\users.json")
            os.rename(new_file, r"game_files\classes\json\users.json")
            os.system("cls")

star.check_dupe_or_append("ex",char)