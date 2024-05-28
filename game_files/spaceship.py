with open (r"game_files\classes\json\users.json", "r") as hi : 
    users = json.load(hi)

import sys
sys.path.append(gamefile)
from rand import *
from dialogue import *
import os

class spaceship():
    def welcome(username):
        print("??: Welcome abroad the spaceship! Captain Xingxing, here!")
        random.contin()
        print("Xingxing: Greetings! Is there anything you would like?")
        print([1] Quests)
        for user in users:
            if user['name'] == username:
                data = len(user['quest'])
        if data == 2:
            print("[2] Star System")
            print("[3] Change Team")
        answer = input("")
        a = ["1", "2", "3"]
        while answer not in a:
            print("Xingxing: Choose again! You can't just make your own choices!!")
            answer = input("")
        ## call on functions later......
    def quest(username):
        for user in users:
            if user['name'] == username:
                quests = len(user['quest'])
        worlds = ["spaceship", "monde", "pero", "taiyo"]
        print("Quests chosen...")
        os.system("cls")
        random.load()
        if quests == 1:
            print("You walk towards the transportation and logistics division to begin your next task.")
            print("You feel that you are getting closer to finding your sibling.")
            dialogues_quest.amalthea(0)
            print("[1] Yes")
            print("[2] No")
            a = ["1", "2"]
            answer = input("")
            while answer not in a:
                print("Amalthea: What does that mean? Please be more specific!")
                answer = input("")
            if answer == a[0]:
                dialogues_quest.amalthea(1)
                print("You:...")
                dialogues_quest.amalthea(2)
                dialogues_quest.transition(1)
                random.load()
        else:
                                #import the mission tutorial
            
            
            if quests == 2:
                dialogues_quest.
            elif quests == 3:
                pass
            elif quests == 4:
                pass
    def star_system():
        pass
    def team():
        pass
