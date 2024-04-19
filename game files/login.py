import os
import json

# use data from users.json file idk how to do that

data = [{'username': 'a', 'password': 'abc'}, {'username': 'b', 'password': 'xyz'}]     # examples for testing the code - delete later

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

    def admin():
        username = input("Enter admin username: ")   # do i even need to make a separate one for admin
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
    
login.player()  # function works in this file, dk to how incorporate data from users.json
