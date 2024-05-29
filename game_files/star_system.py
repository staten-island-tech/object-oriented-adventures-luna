
#import stuff
import os
import json
import random
with open (r"game_files\classes\json\entities.json", "r") as bye :
    entities = json.load(bye)
with open (r"game_files\classes\json\users.json", "r") as hi:
    users = json.load(hi)


class star():
    k = 15
    def view_characters(username):
        a = 0
        for user in users:
            if user['username'] == username:
                characters = user['characters']
                print("You currently have these characters: ")
                for i in characters:
                    print(i)
            else:
                a += 1


    def check_dupe_or_append(username,character):
        for i in users:
            if i['username'] == username:
                if character in i['characters']:
                    i['crystals'] += 80
                    i['stars'] += 1
                else:
                    del i['characters']
                    i['characters'].append(character)
                    i['stars'] += 1
                    new_file = "updated.json"
                    with open(new_file, "w") as f:
                        json_string = json.dumps(users)
                        f.write(json_string)
                    os.remove(r"game_files\classes\json\users.json")
                    os.rename(new_file, r"game_files\classes\json\users.json")

    def get_random_character(k,n):                 # k = 15 --> represents the percent chance of pulling a character
                                                 # n is the username of the user who is pulling the characters --> becomes username in the pull_one and pull_ten functions

        character = random.choices(entities).pop()
        print(character)
        list_b = [random.randint(1,100) for i in range(k)]       #generates a list of 15 random int btwn 1-100
        b = random.randint(1,100)           # generate 1 random int btwn 1-100
        if b in list_b:                     #15% chance of occurring        
            if character['rarity'] == "*****":
                the_number = random.randint(1,100)
                c = random.randint(1,100)                 #1 percent chance of this happening
                if c == the_number:
                    print(f"Congrats! You pulled a five-star character")
                    print(character)
                    star.check_dupe_or_append(n,character)
                else:
                    print("oh no! you lost ur five-star :(")
            else:
                the_number = [random.randint(1,100) for i in range(99)]
                c = random.randint(1,100)
                if c in the_number:
                    print(f"Congrats! You pulled a four-star character")
                    print(character)
                    star.check_dupe_or_append(n,character)
        else: 
                    print("you got nothing hahahahah")
                  

    def soft_pity(k,username):
        for user in users:
            if user['username'] == username:
                star_counter = user['stars']
        while star_counter == 70:
            n = random.randint(5,10)          # n is the percentage the rate for characters will increase by
            k = k + n
            star.get_random_character(k,username)   # m is the new, increased percentage


    def hard_pity(k,username):
        for user in users:
            if user['username'] == username:
                star_counter = user['stars']
        while star_counter == 80:
            n = random.randint(15,20)          # n is the percentage the rate for characters will increase by
            k = k + n
            star.get_random_character(k,username)   # m is the new, increased percentage


    def super_hard_pity(username):
        for user in users:
            if user['username'] == username:
                star_counter = user['stars']
        while star_counter == 90:
            star.get_random_character(100,username)
        
    def activate_pity(k,username):
        star.soft_pity(k,username)
        star.hard_pity(k,username)
        star.super_hard_pity(username)

    def pull_one(username):
        k = star.k

        #star.       #next steps: use activate inside pull_one or vice versa and add versions
        a = 0
        for user in users:
            if user['username'] == username:
                crystals = user['crystals']
                characters = user['characters']
                print(f"{username} currently has {crystals} crystals")
        if crystals < 160:
            print("You do not have enough crystals.")
        else: 
            answer = input("are you sure you want to use 160 crystals? y/n ").lower()
            while answer != "n" and answer != "y":
                answer = input("are you sure you want to use 160 crystals? y/n ").lower()
            while answer == "y":
                crystals -= 160
                star.get_random_character(k,username)
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

        print(f"{username} now has {crystals} crystals left")
        print(f"Your current characters: {characters}")
        print(f"you used {user['stars']} stars")




    def pull_ten(username):
        a = 0
        k = star.k
        for user in users:
            if user['username'] == username:
                crystals = user['crystals']
                print(f"{username} currently has {crystals} crystals")
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
                    star.get_random_character(k,username)
                    count += 1

            if answer == "n":
                retry = "n"
            while retry != "y" and retry != "n":
                retry = input("pull again? y/n ").lower()
            while retry == "y":
                star.pull_one(username)
            answer = "n"

        print(f"{username} now has {crystals} crystals left")
        print(f"Your current characters: {user['characters']}")
        print(f"you used {user['stars']} stars")

        # subtract 1600 crystals
        #if not enough, go to do mission
        #choose random character 10 times
        #check for dupe each time: if yes add 80 crystals
        #if no append to user data
        

star.pull_one("exa")
