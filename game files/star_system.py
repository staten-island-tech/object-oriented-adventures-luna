
#import stuff

import json
import random
test = open(r"game files\classes\json\entities.json", encoding="utf8")
entities = json.load(test)

users = [
    {
        'username': "example",
        "password": "123",
        "type": "player",
        "team_lvl": 1,
        'crystals': 200,
        "stars": 0,
        "character": []
    },
    {
        "username": "examplee",
        "password": "abc",
        "type": "player",
        "team_lvl": 1,
        "crystals": 200,
        "stars": 0,
        "character": []
    },
    {
        "username": "exampleee",
        "password": "abc",
        "type": "player",
        "team_lvl": 1,
        "crystals": 0,
        "stars": 0,
        "character": []
    }
]

star_counter = 0

class star():
    global star_counter
    def soft_pity():
        while star_counter == 70:
            #k = 
            pass
            #increase rate
    
    def check_dup_characters(user,character):
        a = 0
        for i in users:
            while i['name'] != user:
                a += 1
            if character in i['character']:
                i['crystals'] += 80
            else:
                i['character'].append(character)


    def pull_one(usernam):
        global star_counter
        a = 0
        for user in users:
            while user['username'] != usernam:
               a += 1
            crystals = user['crystals']
            print(f"{usernam} currently has {crystals} crystals")
            return
        if crystals < 160:
            print("You do not have enough crystals.")
        else: 
            answer = input("are you sure you want to use 160 crystals? y/n ").lower()
            while answer != "n" and answer != "y":
                answer = input("are you sure you want to use 160 crystals? y/n ").lower()
            while answer == "y":
                
                crystals -= 160
                character = random.choices(entities).pop()
                print(character)
                k = 15
                list_b = [random.randint(1,100) for i in range(k)]       #generates a list of 15 random int btwn 1-100
                b = random.randint(1,100)           # generate 1 random int btwn 1-100
                if b in list_b:                     #15% chance of occurring
                    
                    if character['rarity'] == "*****":
                        the_number = random.randint(1,100)
                        c = random.randint(1,100)                 #1 percent chance of this happening
                        if c == the_number:
                            print(f"Congrats! You pulled a five-star character")
                            print(character)
                            star.check_dup_characters(usernam,character)
                        else:
                            print("oh no! you lost ur five-star :(")
                    else:
                        the_number = [random.randint(1,100) for i in range(99)]
                        c = random.randint(1,100)
                        if c in the_number:
                            print(f"Congrats! You pulled a four-star character")
                            print(character)
                            star.check_dup_characters(usernam,character)
                else: 
                    print("you got nothing hahahahah")
                    retry = input("pull again? y/n ").lower()
                    if retry == "n":
                        answer = "n"
            if answer == "n":
                retry = "n"
            while retry != "y" and retry != "n":
                retry = input("pull again? y/n ").lower()
            while retry == "y":
                star.pull_one(usernam)
            answer = "n"

        star_counter += 1
        print(f"{usernam} now has {crystals} crystals left")
        print(f"Your current characters: {user['character']}")
        print(f"you used {star_counter} stars")


        

    def pull_ten(usernam):
        a = 0
        for user in users:
            while user['username'] != usernam:
               a += 1
            crystals = user['crystals']
            print(f"{usernam} currently has {crystals} crystals")
            return
        if crystals < 1600:
            print("You do not have enough crystals.")
        
        else: 
            answer = input("are you sure you want to use 1600 crystals? y/n ").lower()
            while answer != "n" and answer != "y":
                answer = input("are you sure you want to use 1600 crystals? y/n ").lower()
            while answer == "y":
                crystals -= 1600
                pull_list
                character = random.choices(entities).pop()
                print(character)
                k = 15
                list_b = [random.randint(1,100) for i in range(k)]       #generates a list of 15 random int btwn 1-100
                b = random.randint(1,100)           # generate 1 random int btwn 1-100
                if b in list_b:                     #15% chance of occurring
                    
                    if character['rarity'] == "*****":
                        the_number = random.randint(1,100)
                        c = random.randint(1,100)                 #1 percent chance of this happening
                        if c == the_number:
                            print(f"Congrats! You pulled a five-star character")
                            print(character)
                            star.check_dup_characters(usernam,character)
                        else:
                            print("oh no! you lost ur five-star :(")
                    else:
                        the_number = [random.randint(1,100) for i in range(99)]
                        c = random.randint(1,100)
                        if c in the_number:
                            print(f"Congrats! You pulled a four-star character")
                            print(character)
                            star.check_dup_characters(usernam,character)
                else: 
                    print("you got nothing hahahahah")
                    retry = input("pull again? y/n ").lower()
                    if retry == "n":
                        answer = "n"
            if answer == "n":
                retry = "n"
            while retry != "y" and retry != "n":
                retry = input("pull again? y/n ").lower()
            while retry == "y":
                star.pull_one(usernam)
            answer = "n"

        star_counter += 1
        print(f"{usernam} now has {crystals} crystals left")
        print(f"Your current characters: {user['character']}")
        print(f"you used {star_counter} stars")

        # subtract 1600 crystals
        #if not enough, go to do mission
        #choose random character 10 times
        #check for dupe each time: if yes add 80 crystals
        #if no append to user data
        

star.pull_one("example")
