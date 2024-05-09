
#import stuff

import json
import random
test = open(r"C:\Users\christina.chen23\Documents\GitHub\object-oriented-adventures-luna\game files\classes\json\entities.json", encoding="utf8")
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
        while crystals < 160:
            print("You do not have enough crystals.")
        crystals -= 160
        print(f"{usernam} now has {crystals} crystals left")
            
        """ 
        r = [85.875, 14.125*0.99125, 14.125*0.00875]
        results = random.choices(("nothing", ), weights=(r[0],r[1],r[2]), k=1) """

        results = random.choice(entities)
        user['character'].append(results)
        print(user['character'])
        
         #subtract 160 crystals from user
        #if not enough, go to do mission
        #choose random character, use rates
        # check for dupes: if yes, add 80 crystals
        # if no, append character to user data

        

    def pull_ten(usernam):
        a = 0
        for user in users:
            while user['username'] != usernam:
               a += 1
            crystals = user['crystals']
            print(f"{usernam} currently has {crystals} crystals")
            break
        while crystals < 1600:
            print("You do not have enough crystals.")
        crystals -= 1600
        print(f"{usernam} now has {crystals} crystals left")
            
        """ 
        r = [85.875, 14.125*0.99125, 14.125*0.00875]
        results = random.choices(("nothing", ), weights=(r[0],r[1],r[2]), k=1) """

        results = random.choice(entities, k=10)
        user['character'].append(results)
        # subtract 1600 crystals
        #if not enough, go to do mission
        #choose random character 10 times
        #check for dupe each time: if yes add 80 crystals
        #if no append to user data
        

star.pull_one("example")
