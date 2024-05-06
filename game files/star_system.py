""" 
#import stuff
import json
import os
users = open(r"\object-oriented-adventures-luna\classes\users.json", encoding="utf8")
user_data = json.load(users)
 """

user = [
    {
        "username": "example",
        "password": "123",
        "type": "player",
        "version": 0,
        "team_lvl": 1,
        "crystals": 0,
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

    def pull_one(num):
        user[1["crystals"]] -= 160 #subtract 160 crystals from user
        #if not enough, go to do mission
        #choose random character, use rates
        # check for dupes: if yes, add 80 crystals
        # if no, append character to user data
        return user[1["crystals"]]

    def pull_ten(user):
        # subtract 1600 crystals
        #if not enough, go to do mission
        #choose random character 10 times using while loop or something
        #check for dupe each time: if yes add 80 crystals
        #if no append to user data
        pass

star.pull_one()