import json
with open (r"game_files\classes\json\users.json", "r") as hi : 
    users = json.load(hi)

import sys
sys.path.append('gamefile')
from rand import *
from dialogues import *
import os
from battle import *

class spaceship():
    def welcome(username):
        print("??: Welcome abroad the spaceship! Captain Xingxing, here!")
        random.contin()
        print("Xingxing: Greetings! Is there anything you would like?")
        for user in users:
            if user['username'] == username:
                if len(user['quest']) == 0:
                    pass                    ## import prologue
        print("[1] Quests")
        for user in users:
            if user['username'] == username:
                data = len(user['quest'])
        if data == 2:
            print("[2] Star System")
            print("[3] Change Team")
        answer = input("")
        a = ["1", "2", "3"]
        while answer not in a:
            print("Xingxing: Choose again! You can't just make your own choices!!")
            answer = input("")
        print("Xingxing: Hmm. Alright then. Let's go.")
        if answer == "1":
            print("Xingxing: What type of mission are you going on this time?")
            random.quest_selector(username)
            b = ["S", "B"]
            quest = input("").upper()
            while quest not in b:
                print("Xingxing: What did I say! What do you want to do anyways!?")
                quest = input("").upper()
            print("Xingxing: Hmm...I see.")
        random.load()
    def quest_story(username):
        for user in users:
            if user['username'] == username:
                quests = len(user['quest'])
        print("Story Quests chosen...")
        random.contin()
        os.system("cls")
        random.load()
        print("You walk towards the transportation and logistics division to begin your next task.")
        print("You feel that you are getting closer to finding your sibling.")
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
                os.system()
                dialogues_quest.amalthea(1)
                print("You:...")
                dialogues_quest.amalthea(2)
                dialogues_quest.transition(1)
                random.load()
            if answer == a[1]:
                print("Amalthea: I see")
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
                random.contin()
                print("You: You too, Lyra.")
                random.contin()
                dialogues_quest.lyra(2)
                random.contin()
                dialogues_quest.transition(1)
                random.load()
            if answer == a[1]:
                print("Lyra: Alright. Enjoy your time exploring the spaceship then new recruit!")
                os.system("cls")
                print("Lyra: The observatory at the front of this spacecraft is absolutely wonderful! Be sure to see it!")
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
                random.contin()
                print("You: I will. see you when I come back then, Astrophel!")
                random.contin()
                dialogues_quest.astrophel(2)
                random.contin()
                dialogues_quest.transition(1)
                random.load()
            if answer == a[1]:
                print("Astrophel: Oh. Alright! Please enjoy your time on the spaceship then!")
        elif quests == 4:
            print("Looking around you find yourself at the transportation and logistics department once more.")
            random.contin()
            print("Lyra: Oh. Hi, what are you doing here new recruit? There isn't any other tasks for you so far.")
            random.contin()
            print("You: ...")
            random.contin()
            print("Lyra: You must have gotten used to coming here...")
            random.contin()
            print("Nodding, you leave the division to wander the large endless spaceship.")
        else:
            print("Wow. You are too weak for this, player!")
            random.contin()
            print("Going back to the main lobby...")
            os.system("cls")
            random.load()
            spaceship.welcome(username)
    def daily(username):
        print("Dailies Chosen...")
        os.system("cls")
        random.load()
        print("You walk towards the holo-reality, a virtual reality simulator on the spaceship used for training.")

    def star_system():
        pass
    def team():
        

spaceship.quest_story("exa")