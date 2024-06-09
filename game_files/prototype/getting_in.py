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

with open (r"game_files/classes/json/users.json", "r") as hi : 
    users = json.load(hi)

with open (r"game_files/classes/json/entities.json", "r") as bye :
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
                for user in users:
                    if user['username'] == username:
                        data = len(user['quest'])
                if data == 0:
                    print("Continuing story quest...")
                    rand.contin()
                    prologue.path(username)
                    pro.wel(username)
                else:
                    print("Transporting back to spaceship...")
                    rand.contin()
                    pro.wel(username)
            if account == "2":
                login.signup()
                os.system("cls")
                username = input("What is your username? ")
                print("Welcome to our Game!")
                print("Thank you for playing this game! To show our apprieciation we will be giving you 12,800 crystals!")
                print("This will be useful to you later on in the game! You will also be getting a free four-star character when you start.")
                print("This character will be Asahi who you will meet later on in the game.")
                print("Thank you for your time! Have fun!")
                rand.contin()
                prologue.newbeginnings()
                prologue.path(username)
                pro.wel(username)
            a = "n"
