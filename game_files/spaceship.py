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
        if data >= 2:
            print("[2] Star System")
            print("[3] Change Team")

    def quest_story(username):
        for user in users:
            if user['username'] == username:
                quests = len(user['quest'])
        print("Story Quests chosen...")
        rand.contin()
        os.system("cls")
        rand.load()
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
                rand.load()
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
                rand.load()
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
                rand.load()
                taiyo.path(username)
            elif answer == a[1]:
                print("Astrophel: Oh. Alright! Please enjoy your time on the spaceship then!")
                rand.contin()
                pass
        elif quests == 4:
            print("Looking around you find yourself at the transportation and logistics department once more.")
            rand.contin()
            print("Lyra: Oh. Hi, what are you doing here new recruit? There isn't any other tasks for you so far.")
            rand.contin()
            print("You: ...")
            rand.contin()
            print("Lyra: You must have gotten used to coming here...")
            rand.contin()
            print("Nodding, you leave the division to wander the large endless spaceship.")
            rand.contin()
            pass
        else:
            print("Wow. You are too weak for this, player!")
            rand.contin()
            print("Going back to the main lobby...")
            os.system("cls")
            rand.load()
            pass

    def daily(username):
        print("Dailies Chosen...")
        rand.contin()
        rand.load()
        print("You walk towards the holo-reality, a virtual reality simulator on the spaceship used for training.")
        rand.contin()
        dialogues_quest.adhara(0)
        print("[1] Yes")
        print("[2] No")
        a = input("")
        b = ["1", "2"]
        while a not in b:
            print("Adhara: What do you mean?")
            a = input("")
        if a == b[0]:
            os.system("cls")
            print("Which world would you like to challenge again?")
            quests = []
            for user in users:
                if user['username'] == username:
                    quests = [user['quests']]
            letter = ["A", "B", "C", "D", "E"]
            length = len(quests)
            y = 0
            x = letter[y]
            z = 1
            letters = []
            for i in range(length):
                print(f"[{x}] {quests[z]}")
                letters.append(x)
                y += 1
                z += 1
            answer = input("").upper()
            while answer not in letters:
                print("You haven't unlocked this world yet!!")
                rand.contin()
                print("Please choose again.")
                rand.contin()
                for i in range(length):
                    print(f"[{x}] {quests[z]}")
                    y += 1
                    z += 1
                answer = input("").upper()
            if answer in letters:
                y = 0
                number = 0
                for l in letters:
                    if l == x:
                        number = y + 1
                    y += 1
                dialogues_quest.adhara(1)
                rand.contin()
                dialogues_quest.adhara(2)
                rand.contin()
                rand.load()
                pass
        elif a == b[1]:
            print("Adhara: Alright then. Have fun on the spaceship!")
            rand.contin()
            pass

    def star_system(username):
        with open (r"game_files/classes/json/users.json", "r") as hi : 
            users = json.load(hi)

        with open (r"game_files/classes/json/entities.json", "r") as bye :
            entities = json.load(bye)
        print("Welcome to the star system - what would you like to do?")
        print("[1] View your characters")
        print("[2] Buy 1 star and pull once")
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

