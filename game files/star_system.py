
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
    
    def check_dup_characters(user,character):
        a = 0
        for i in users:
            while i['name'] != user:
                a += 1
            if character in i['character']:
                i['crystals'] += 80
            else:
                i['character'].append(character)

    def get_random_character(k,n):                 # k = 15 --> represents the percent chance of pulling a character
                                                 # n is the username of the user who is pulling the characters --> becomes username in the pull_one and pull_ten functions
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
                    star.check_dup_characters(n,character)
                else:
                    print("oh no! you lost ur five-star :(")
            else:
                the_number = [random.randint(1,100) for i in range(99)]
                c = random.randint(1,100)
                if c in the_number:
                    print(f"Congrats! You pulled a four-star character")
                    print(character)
                    star.check_dup_characters(n,character)
        else: 
                    print("you got nothing hahahahah")

    def soft_pity(k,username):
        while star_counter == 70:
            n = random.randint(5,10)          # n is the percentage the rate for characters will increase by
            m = k + n
            star.get_random_character(m,username)   # m is the new, increased percentage


    def hard_pity(k,username):
        while star_counter == 80:
            n = random.randint(15,20)          # n is the percentage the rate for characters will increase by
            m = k + n
            star.get_random_character(m,username)   # m is the new, increased percentage


    def super_hard_pity(username):
        while star_counter == 90:
            star.get_random_character(100,username)
        
    def activate(k,username):
        star.soft_pity(k,username)
        star.hard_pity(k,username)
        star.super_hard_pity(username)

    def pull_one(username):
        global star_counter
        star.       #next steps: use activate inside pull_one or vice versa
        a = 0
        for user in users:
            while user['username'] != username:
               a += 1
            crystals = user['crystals']
            print(f"{username} currently has {crystals} crystals")
            return
        if crystals < 160:
            print("You do not have enough crystals.")
        else: 
            answer = input("are you sure you want to use 160 crystals? y/n ").lower()
            while answer != "n" and answer != "y":
                answer = input("are you sure you want to use 160 crystals? y/n ").lower()
            while answer == "y":
                crystals -= 160
                star.get_random_character(15,username)
                retry = input("pull again? y/n ").lower()
                if retry == "n":
                    answer = "n"
            if answer == "n":
                retry = "n"
            while retry != "y" and retry != "n":
                retry = input("pull again? y/n ").lower()
            while retry == "y":
                star.pull_one(username)
            answer = "n"

        star_counter += 1
        print(f"{username} now has {crystals} crystals left")
        print(f"Your current characters: {user['character']}")
        print(f"you used {star_counter} stars")



    def pull_ten(username):
        a = 0
        global star_counter
        for user in users:
            while user['username'] != username:
               a += 1
            crystals = user['crystals']
            print(f"{username} currently has {crystals} crystals")
            return
        if crystals < 1600:
            print("You do not have enough crystals.")
        
        else: 
            answer = input("are you sure you want to use 1600 crystals? y/n ").lower()
            while answer != "n" and answer != "y":
                answer = input("are you sure you want to use 1600 crystals? y/n ").lower()
            while answer == "y":
                crystals -= 1600
                count = 0
                while count < 10:
                    star.get_random_character(15,username)
                    count += 1

            if answer == "n":
                retry = "n"
            while retry != "y" and retry != "n":
                retry = input("pull again? y/n ").lower()
            while retry == "y":
                star.pull_one(username)
            answer = "n"

        star_counter += 10
        print(f"{username} now has {crystals} crystals left")
        print(f"Your current characters: {user['character']}")
        print(f"you used {star_counter} stars")

        # subtract 1600 crystals
        #if not enough, go to do mission
        #choose random character 10 times
        #check for dupe each time: if yes add 80 crystals
        #if no append to user data
        

star.pull_one("example")
