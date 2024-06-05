import os
import json
import random

with open (r"game_files\classes\json\users.json", "r") as hi : 
    users = json.load(hi)

with open (r"game_files\classes\json\entities.json", "r") as bye :
    entities = json.load(bye)

char = {
                "name": "bobby",
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
    k = 30

    def view_characters(username):            #tested
        for user in users: 
            if user['username'] == username:
                characters = user['characters']
                print(f"{username} currently has these characters: ")
                for i in characters:
                    print(i)

    def check_dupe_or_append(username, char):       #char is the entire character dictionary of that character (automatically replaced w variable in function)
        for user in users:                          #tested except for crystals & stars not being added
            if user['username'] == username:
                characters = user['characters']
                crystals = user['crystals']
                stars = user['stars']
        names = []
        for character in characters:
            names.append(character['name'])
        if char['name'] in names:
            crystals += 80                                 #check why this part doesn't work - the characters are appending to list but the numbers are being added
            stars += 1
            print(f"{username} now has {crystals} crystals and {stars} stars.")
            new_file = "updated.json"
            with open(new_file, "w") as f:
                json_string = json.dumps(users)
                f.write(json_string)
            os.remove(r"game_files\classes\json\users.json")
            os.rename(new_file, r"game_files\classes\json\users.json")
            #os.system("cls")
        else: 
            characters.append(char)
            stars += 1
            print(f"{username} now has {crystals} crystals and {stars} stars.")
            new_file = "updated.json"
            with open(new_file, "w") as f:
                json_string = json.dumps(users)
                f.write(json_string)
            os.remove(r"game_files\classes\json\users.json")
            os.rename(new_file, r"game_files\classes\json\users.json")
            #os.system("cls")

    def get_random_character(k,n)                  # k = 30 --> represents the percent chance of pulling a character
                                                 # n is the username of the user who is pulling the characters --> becomes username in the pull_one and pull_ten functions
        character = random.choices(entities).pop()      #randomly chooses a character from entities list
        num_list = [random.randint(1,100) for i in range(k)]    # generates a list of 15 random int btwn 1-100
        b = random.randint(1,100)                  # generate 1 random int btwn 1-100
        if b in num_list:               # 30% chance of occurring
            print(character)
            print(f"Congrats! ")

star.check_dupe_or_append("ex",char)

