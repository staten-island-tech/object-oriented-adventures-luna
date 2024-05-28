
## call in the json files and other programs(login and loading screen)
import json
import os

from classes import login
from entry import *
from rand import *

with open (r"game_files\classes\json\users.json", "r") as hi : 
    users = json.load(hi)

with open (r"game_files\classes\json\entities.json", "r") as bye :
    entities = json.load(bye)


class prototype():
    def start():
        print("Welcome to Legacy!")
        a = input("Is your terminal in full screen? y/n").lower()
        b = ["y", "n"]
        while a not in b:
            a = input("Is your terminal in full screen? y/n").lower()
        while a == "n":
            print("Please put your terminal in full screen.")
            a = input("Is your terminal in full screen now? y/n").lower()
        while a == "y":
            os.system("cls")
            entry.loading()
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
                print("[1] Sign in")
                print("[2] Sign up")
                account = input("")
            if account == "1":
                username = input("What is your username? ")
                login.player(username)
                os.system("cls")
                print("Welcome back!")
                os.system("cls")
                random.load()
                for user in users:
                    if user['name'] == username:
                        data = len(user['quest'])
                if data == 0:
                    pass                     ## import prologue and spaceship/tutorial battles
                else:
                    print("Transporting back to spaceship...")
                    c = input("[A] Continue").upper()
                    while c != "A":
                        c = input("").upper()
                    if c == "A":
                        pass                   ## import spaceship code
            if account == "2":
                login.signup()
                os.system("cls")
                random.load()
                                    ##  import prologue
