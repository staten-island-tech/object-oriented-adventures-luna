import os
import json
import random
import time
from rand import rand

""" with open (r"game_files/classes/json/users.json", "r") as hi : 
    users = json.load(hi)

with open (r"game_files/classes/json/entities.json", "r") as bye :
    entities = json.load(bye) """


class base_functions():         # ***DONT IMPORT OR USE THIS IN OTHER FILES, ONLY USE the  starsystem class
    def check_dupe_or_append(username, character):       #char is the entire character dictionary of that character (automatically replaced w variable in function)
        with open (r"game_files/classes/json/users.json", "r") as hi : 
            users = json.load(hi)
        for user in users:                         #tested
            if user['username'] == username:
                characters = user['characters']
                if character['name'] in characters:
                    print("you already have this character so you get 80 crystals instead")
                    user['crystals'] += 80
                    user['stars'] += 1
                else: 
                    characters.append(character['name'])
                    user['stars'] += 1
                if user['stars'] > 90:
                    user['stars'] = 0
                else:
                    pass
        new_file = "updated.json"
        with open(new_file, "w") as f:
            json_string = json.dumps(users)
            f.write(json_string)
        os.remove(r"game_files/classes/json/users.json")
        os.rename(new_file, r"game_files/classes/json/users.json")
        #os.system("cls")

    def get_random_character(k,n):                  # k = 30 --> represents the percent chance of pulling a character
                                                 # n is the username of the user who is pulling the characters --> becomes username in the pull_one and pull_ten functions
        with open (r"game_files/classes/json/users.json", "r") as hi : 
            users = json.load(hi)
        with open (r"game_files/classes/json/entities.json", "r") as bye :
            entities = json.load(bye)
        
        char_list = []
        for user in users:
            if user['username'] == n:
                if user['stars'] >= 90:
                    for entity in entities[0:19]:
                        if entity['rarity'] == "*****":
                            char_list.append(entity)
                        else:
                            pass
                else:
                    for entity in entities[0:19]:
                        char_list.append(entity)
        character = random.choices(char_list).pop()      #randomly chooses a character from entities list, includes the entire dict
        num_list = [random.randint(1,100) for i in range(k)]    # generates a list of 30 random int btwn 1-100
        b = random.randint(1,100)                  # generate 1 random int btwn 1-100
        if b in num_list:               # 30% chance of occurring
            print(character)
            print(f"Congrats! You pulled {character['name']}")
            base_functions.check_dupe_or_append(n,character)
        else:
            print("you got nothing hahahahah")
            for user in users:
                if user['username'] == n:
                    user['stars'] += 1

            new_file = "updated.json"
            with open(new_file, "w") as f:
                json_string = json.dumps(users)
                f.write(json_string)
            os.remove(r"game_files/classes/json/users.json")
            os.rename(new_file, r"game_files/classes/json/users.json")

    def activate_pity(username):
        with open (r"game_files/classes/json/users.json", "r") as hi : 
            users = json.load(hi)
        k = starsystem.k
        for user in users:
            if user['username'] == username:
                if 70 <= user['stars'] < 80:
                    k += random.randint(5,10)
                elif 80 <= user['stars'] < 90:
                    k += random.randint(15,20)
                elif user['stars'] > 90:
                    k = 100
                else:
                    pass

                    



class starsystem():
    k = 30

    def view_characters(username):            #tested
        with open (r"game_files/classes/json/users.json", "r") as hi : 
            users = json.load(hi)
        for user in users: 
            if user['username'] == username:
                characters = user['characters']
                print(f"{username} currently has these characters: ")
                for i in characters:
                    print(i)
        
    def pull_one(username):            #tested
        with open (r"game_files/classes/json/users.json", "r") as hi : 
            users = json.load(hi)
        k = starsystem.k
        base_functions.activate_pity(username)
        for user in users:
            if user['username'] == username:
                print(f"{username} currently has {user['crystals']} crystals")
                if user['crystals'] < 160:
                    print("you do not have enough crystals.")
                else: 
                    answer = input("are you sure you want to use 160 crystals? y/n ").lower()
                    while answer != "n" and answer != "y":
                        answer = input("are you sure you want to use 160 crystals? y/n ").lower()
                    while answer == "y":
                        user['crystals'] -= 160
                        new_file = "updated.json"
                        with open(new_file, "w") as f:
                            json_string = json.dumps(users)
                            f.write(json_string)
                        os.remove(r"game_files/classes/json/users.json")
                        os.rename(new_file, r"game_files/classes/json/users.json")
                        base_functions.get_random_character(k,username)
                        answer = "n"
                with open (r"game_files/classes/json/users.json", "r") as hi : 
                    users = json.load(hi)
                print(f"{username} now has {user['crystals']} crystals left")

    def pull_ten(username):            #tested
        with open (r"game_files/classes/json/users.json", "r") as hi : 
            users = json.load(hi)
        k = starsystem.k
        base_functions.activate_pity(username)

        for user in users:
            if user['username'] == username:
                print(f"{username} currently has {user['crystals']} crystals")
                if user['crystals'] < 1600:
                    print("you do not have enough crystals.")
                else: 
                    answer = input("are you sure you want to use 1600 crystals? y/n ").lower()
                    while answer != "n" and answer != "y":
                        answer = input("are you sure you want to use 1600 crystals? y/n ").lower()
                    while answer == "y":
                        user['crystals'] -= 1600
                        new_file = "updated.json"
                        with open(new_file, "w") as f:
                            json_string = json.dumps(users)
                            f.write(json_string)
                        os.remove(r"game_files/classes/json/users.json")
                        os.rename(new_file, r"game_files/classes/json/users.json")
                        count = 0
                        othercount = 1
                        while count < 10:
                            print(f"--PULL NUMBER {othercount}: --")
                            time.sleep(0.25)
                            base_functions.get_random_character(k,username)
                            rand.contin()
                            count += 1
                            othercount += 1
                        answer = "n"
                with open (r"game_files/classes/json/users.json", "r") as hi : 
                    users = json.load(hi)
                print(f"{username} now has {user['crystals']} crystals left")