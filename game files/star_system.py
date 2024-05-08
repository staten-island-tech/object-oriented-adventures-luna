
#import stuff

import json
# Open the JSON file of pokemon data
test = open(r"C:\Users\christina.chen23\Documents\GitHub\object-oriented-adventures-luna\game files\classes\entities.json", encoding="utf8")
# create variable "data" that represents the enitre pokedex list
entities = json.load(test)

users = [
    {
        'username': "example",
        "password": "123",
        "type": "player",
        "version": 0,
        "team_lvl": 1,
        'crystals': 500,
        "stars": 0,
        "character": []
    },
    {
        "username": "examplee",
        "password": "abc",
        "type": "player",
        "version": 0,
        "team_lvl": 1,
        "crystals": 200,
        "stars": 0,
        "character": []
    },
    {
        "username": "exampleee",
        "password": "abc",
        "type": "player",
        "version": 0,
        "team_lvl": 1,
        "crystals": 0,
        "stars": 0,
        "character": []
    }
]

star_counter = 0

class star():
    import random
    
    def soft_pity():
        while star_counter == 70:
            pass
            #increase

    def pull_one(usernam):
        a = 0
        for user in users:
            while user['username'] != usernam:
               a += 1
            crystals = user['crystals']
            print(f"{usernam} currently has {crystals} crystals")
            break
        if crystals > 160:
            crystals -= 160
            print(f"{usernam} now has {crystals} crystals left")
        else:
            print("You do not have enough crystals.")
        rare = []
        super_rare = []
        for i in entities:
            if i["rarity"] == "****":
                rare.append(i)
            else:
                super_rare.append(i)
        rates = [0.85875, 0.14125*0.99125, 0.14125*0.00875]

    

        
         #subtract 160 crystals from user - DONE
        #if not enough, go to do mission
        #choose random character, use rates
        # check for dupes: if yes, add 80 crystals
        # if no, append character to user data

        

    def pull_ten(user):
        # subtract 1600 crystals
        #if not enough, go to do mission
        #choose random character 10 times using while loop or something
        #check for dupe each time: if yes add 80 crystals
        #if no append to user data
        pass

star.pull_one("example")
