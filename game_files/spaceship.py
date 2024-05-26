with open (r"game_files\classes\json\users.json", "r") as hi : 
    users = json.load(hi)

import sys
sys.path.append(gamefile)
from rand import *
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
        
    def quest(username):
        for user in users:
            if user['name'] == username:
                quests = len(user['quest'])
        worlds = ["spaceship", "pero", "monde", "taiyo"]
        
    def star_system():
        pass
    def team():
        pass
