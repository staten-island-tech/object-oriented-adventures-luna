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

data_users = open("./game_files/classes/json/users.json", encoding="utf8")
users = json.load(data_users)

data_entities = open("./game_files/classes/json/entities.json", encoding="utf8")
entities = json.load(data_entities)



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
            rand.contin()
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
                    print("Continuing story quest...")
                    rand.contin()
                    prologue.path(username)
                else:
                    print("Transporting back to spaceship...")
                    rand.contin()
                    pro.wel(username)
            if account == "2":
                login.signup()
                os.system("cls")
                rand.load()
                username = input("What is your username? ")
                print("Welcome to our Game!")
                print("Thank you for playing this game! To show our apprieciation we will be giving you 12,800 crystals!")
                rand.contin()
                print("This will be useful to you later on in the game! You will also be getting a free four-staar character when you start.")
                rand.contin()
                print("This character will be Asahi who you will meet later on in the game.")
                rand.contin()
                print("Thank you for your time! Have fun!")
                rand.contin()
                prologue.newbeginnings()
                prologue.path(username)
                pro.wel(username)
            a = "n"
