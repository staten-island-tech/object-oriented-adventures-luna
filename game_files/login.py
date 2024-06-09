from user import create
import json

with open (r"game_files/classes/json/users.json", "r") as hi : 
    users = json.load(hi)




class login():
    def player(username):
        num_matches = []
        for user in users:
            if username == user["username"]:
                num_matches.append(user)
                password = input(f"Enter password for {username}: ")
        if len(num_matches) == 0:
            print("This username does not exist. Please try again ")
            login.player(username)
        for i in num_matches:       # works bc there's only one dictionary in the list since only one username should match
            while password != i['password']:
                print("incorrect password, try again")
                password = input(f"enter password for {username}: ")
        print("Congrats! You have successfully logged in ")
        # and then load that user's data or something idkidkidk
    def signup():
        create.add()
        
