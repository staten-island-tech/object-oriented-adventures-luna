
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
            
        character = random.choices(entities)
        list_b = [random.randint(1,100) for i in range(15)]       #generates a list of 15 random int btwn 1-100
        b = random.randint(1,100)           # generate 1 random int btwn 1-100
        if b in list_b:                     #15% chance of occurring
            if character["rarity"] == "*****":
                the_number = random.randint(1,100)
                c = random.randint(1,100)                 #1 percent chance of this happening
                if c in the_number:
                    print(f"Congrats! You pulled a five-star character")
                    print("")
                    print(character)
                    user['character'].append(character)
                else:
                    print("oh no! you lost ur five-star :(")
            else:
                the_number = [random.randint(1,100) for i in range(99)]
                c = random.randint(1,100)
                if c in the_number:
                    print(f"Congrats! You pulled a four-star character")
                    print("")
                    print(character)
                    user['character'].append(character)
        else: 
            print("you got nothing hahahahah")
            
            b = random.randint(1,100)

        print(f"Your current characters: {user['character']}")
        
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
        
        # subtract 1600 crystals
        #if not enough, go to do mission
        #choose random character 10 times
        #check for dupe each time: if yes add 80 crystals
        #if no append to user data
        

star.pull_one("example")
