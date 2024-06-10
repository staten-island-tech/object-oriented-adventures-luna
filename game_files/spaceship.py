import json
with open (r"game_files/classes/json/users.json", "r") as hi : 
    users = json.load(hi)

with open (r"game_files/classes/json/entities.json", "r") as bye :
    entities = json.load(bye)

import os
from rand import *
from dialogues import *
from battle import *
from star_system import starsystem
from prototype.worlds import *
from prototype.prototype_4 import *

class spaceship():
    def welcome(username):
        with open (r"game_files/classes/json/users.json", "r") as hi : 
            users = json.load(hi)

        with open (r"game_files/classes/json/entities.json", "r") as bye :
            entities = json.load(bye)
        print("??: Welcome abroad the spaceship! Captain Xingxing, here!")
        rand.contin()
        print("Xingxing: Greetings! Is there anything you would like?")
        print("[1] Quests")
        for user in users:
            if user['username'] == username:
                data = len(user['quest'])
        if data >= 1:
            print("[2] Star System")
            print("[3] Change Team")

    def quest_story(username):
        with open (r"game_files/classes/json/users.json", "r") as hi : 
            users = json.load(hi)
        for user in users:
            if user['username'] == username:
                quests = len(user['quest'])
        print("Story Quests chosen...")
        rand.contin()
        os.system("cls")
        print("You walk towards the transportation and logistics division to begin your next task.")
        rand.contin()
        print("You feel that you are getting closer to finding your sibling.")
        rand.contin()
        if quests == 1:
            dialogues_quest.amalthea(0)
            print("[1] Yes")
            print("[2] No")
            a = ["1", "2"]
            answer = input("")
            while answer not in a:
                print("Amalthea: What does that mean? Please be more specific!")
                answer = input("")
            if answer == a[0]:
                os.system('cls')
                dialogues_quest.amalthea(1)
                print("You:...")
                dialogues_quest.amalthea(2)
                rand.contin()
                worlds.monde_mission(username)
            elif answer == a[1]:
                print("Amalthea: I see")
                rand.contin()
                pass
        elif quests == 2:
            dialogues_quest.lyra(0)
            print("[1] Yes")
            print("[2] No")
            a = ["1", "2"]
            answer = input("")
            while answer not in a:
                print("Lyra: Hmm...what's that? Can you please tell me again?")
                answer = input("")
            if answer == a[0]:
                os.system("cls")
                dialogues_quest.lyra(1)
                rand.contin()
                worlds.pero_mission(username)
            elif answer == a[1]:
                print("Lyra: Alright. Enjoy your time exploring the spaceship then new recruit!")
                os.system("cls")
                print("Lyra: The observatory at the front of this spacecraft is absolutely wonderful! Be sure to see it!")
                rand.contin()
                pass
        elif quests == 3:
            dialogues_quest.astrophel(0)
            print("[1] Yes")
            print("[2] No")
            a = ["1", "2"]
            answer = input("")
            while answer not in a:
                print("Astrophel: What did you say?")
                answer = input("")
            if answer == a[0]:
                dialogues_quest.astrophel(1)
                rand.contin()
                print("You: I will. See you when I come back then, Astrophel!")
                rand.contin()
                taiyo.path(username)
            elif answer == a[1]:
                print("Astrophel: Oh. Alright! Please enjoy your time on the spaceship then!")
                rand.contin()
                pass
        elif quests == 4:
            print("Looking around you find yourself at the transportation and logistics department once more.")
            print("Lyra: Oh. Hi, what are you doing here new recruit? There isn't any other tasks for you so far.")
            rand.contin()
            print("You: ...")
            rand.contin()
            print("Lyra: You must have gotten used to coming here...")
            print("Nodding, you leave the division to wander the large endless spaceship.")
            rand.contin()
            pass
        else:
            print("Wow. You are too weak for this, player!")
            rand.contin()
            print("Going back to the main lobby...")
            os.system("cls")
            pass

    def star_system(username):
        with open (r"game_files/classes/json/users.json", "r") as hi : 
            users = json.load(hi)
        print("Welcome to the star system - what would you like to do?")
        print("[1] View your characters")
        print("[2] Buy 1 star and pull onces")
        print("[3] Buy 10 stars and pull 10 times")
        answer = input("")
        z = ["1", "2", "3"]
        while answer not in z:
            print("Choose again! You can't just make your own choices!!")
            answer = input("")
        if answer == "1":
            os.system("cls")
            starsystem.view_characters(username)
        elif answer == "2":
            os.system("cls")
            starsystem.pull_one(username)
        elif answer == "3":
            os.system("cls")
            starsystem.pull_ten(username)
        else:
            pass
    def team(username):
        with open (r"game_files/classes/json/users.json", "r") as hi : 
            users = json.load(hi)
        battle.select_character(username)