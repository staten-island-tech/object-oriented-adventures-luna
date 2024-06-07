## call in the json files and other programs(login and loading screen)
import json
import os
import sys

sys.path.append("game_files")
from prototype.getting_started import *

from login import *
from entry import *
from rand import *
from prototype.spaceship_pro import *

with open (r"game_files\classes\json\users.json", "r") as hi : 
    users = json.load(hi)

with open (r"game_files\classes\json\entities.json", "r") as bye :
    entities = json.load(bye)


class prototype():
    def start():
        print("Welcome to Legacy!")
        a = input("Is your terminal in full screen? y/n ").lower()
        b = ["y", "n"]
        while a not in b:
            a = input("Is your terminal in full screen? y/n ").lower()
        while a == "n":
            print("Please put your terminal in full screen.")
            a = input("Is your terminal in full screen now? y/n ").lower()
        while a == "y":
            os.system("cls")
            entry.screen()
            c = input("[A] Continue").upper()
            while c != "A":
                c = input("").upper()
            os.system("cls")
            print("Welcome to our game! Would you like to sign in to your existing account or sign up for a new account?")
            print("[1] Sign in")
            print("[2] Sign up")
            account = input("")
            d = ["1", "2"]
            while account not in d:
                os.system("cls")
                print("Please try again!")
                print("[1] Sign in")
                print("[2] Sign up")
                account = input("")
            if account == "1":
                username = input("What is your username? ")
                login.player(username)
                os.system("cls")
                print("Welcome back!")
                rand.contin()
                rand.load()
                for user in users:
                    if user['username'] == username:
                        data = len(user['quest'])
                if data == 0:
                    prologue.path(username)
                else:
                    print("Transporting back to spaceship...")
                    rand.contin()
                    pro.wel(username)
            elif account == "2":
                login.signup()
                rand.load()
                username = input("What is your username? ")
                
                while username not in users['username']:
                    username = input("try again ")
                print("Welcome back!")
                
                prologue.start(username)
                """ prologue.newbeginnings()
                prologue.path(username)
                pro.wel(username) """
            a = "n"

prototype.start()