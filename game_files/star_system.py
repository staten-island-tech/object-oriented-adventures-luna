import os
import json
import random
import time

with open (r"game_files\classes\json\users.json", "r") as hi : 
    users = json.load(hi)

with open (r"game_files\classes\json\entities.json", "r") as bye :
    entities = json.load(bye)


class base_functions():         # ***DONT IMPORT OR USE THIS IN OTHER FILES, ONLY USE the  starsystem class
    def check_dupe_or_append(username, char):       #char is the entire character dictionary of that character (automatically replaced w variable in function)
        for user in users:                         #tested
            if user['username'] == username:
                characters = user['characters']
                names = []
                for character in characters:
                    names.append(character)
                if char['name'] in names:
                    user['crystals'] += 80
                    user['stars'] += 1
                else: 
                    characters.append(char['name'])
                    user['stars'] += 1
        new_file = "updated.json"
        with open(new_file, "w") as f:
            json.dump(users, f)
        os.remove(r"game_files\classes\json\users.json")
        os.rename(new_file, r"game_files\classes\json\users.json")
        #os.system("cls")

    def get_random_character(k,n):                  # k = 30 --> represents the percent chance of pulling a character
                                                 # n is the username of the user who is pulling the characters --> becomes username in the pull_one and pull_ten functions
        char_list = []
        for entity in entities[0:19]:
            char_list.append(entity)
        character = random.choices(char_list).pop()      #randomly chooses a character from entities list
        num_list = [random.randint(1,100) for i in range(k)]    # generates a list of 15 random int btwn 1-100
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
                json.dump(users, f)
            os.remove(r"game_files\classes\json\users.json")
            os.rename(new_file, r"game_files\classes\json\users.json")

    def activate_pity(username):
        k = starsystem.k
        for user in users:
            if user['username'] == username:
                if 70 <= user['stars'] < 80:
                    k += random.randint(5,10)
                elif 80 <= user['stars'] < 90:
                    k += random.randint(15,20)
                elif user['stars'] >= 90:
                    k = 100
                else:
                    pass
                    



class starsystem():
    k = 30

    def view_characters(username):            #tested
        for user in users: 
            if user['username'] == username:
                characters = user['characters']
                print(f"{username} currently has these characters: ")
                for i in characters:
                    print(i)
        
    def pull_one(username):            #tested
        k = starsystem.k
        base_functions.activate_pity(username)
        for user in users:
            if user['username'] == username:
                print(f"{username} currenty has {user['crystals']} crystals")
                if user['crystals'] < 160:
                    print("you do not have enough crystals.")
                else: 
                    answer = input("are you sure you want to use 160 crystals? y/n ").lower()
                    while answer != "n" and answer != "y":
                        answer = input("are you sure you want to use 160 crystals? y/n ").lower()
                    while answer == "y":
                        user['crystals'] -= 160
                        base_functions.get_random_character(k,username)
                        answer = "n"
                print(f"{username} now has {user['crystals']} crystals left")
                print(f"you used {user['stars']} stars")

    def pull_ten(username):            #tested
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
                        count = 0
                        othercount = 1
                        while count < 10:
                            print(f"--PULL NUMBER {othercount}: --")
                            time.sleep(0.75)
                            base_functions.get_random_character(k,username)
                            count += 1
                            othercount += 1
                        answer = "n"
                print(f"{username} now has {user['crystals']} crystals left")
                print(f"you used {user['stars']} stars")
