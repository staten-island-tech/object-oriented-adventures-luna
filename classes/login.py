from user import *

import json
# Open the JSON file of pokemon data
test = open(r"C:\Users\owner\Documents\GitHub\object-oriented-adventures-luna\classes\users.json", encoding="utf8")
# create variable "data" that represents the enitre pokedex list
data = json.load(test)


class login():
    def player():
        username = input("Enter player username: ")
        num_matches = []
        for user in data:
            if username in user["username"]:
                num_matches.append(user)
                password = input(f"Enter password for {username}: ")
        if len(num_matches) == 0:
            print("This username does not exist. Please try again ")
            login.player()
        for i in num_matches:       # works bc there's only one dictionary in the list since only one username should match
            while i['password'] != password:
                print("incorrect password, try again")
                password = input(f"enter password for {username}: ")
        print("Congrats! You have successfully logged in ")
        # and then load that user's data or something idkidkidk

    def signup():
        add()

login.add()  