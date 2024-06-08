from user import create
import json

data_users = open("./game_files/classes/json/users.json", encoding="utf8")
users = json.load(data_users)



class login():
    def player(username):
        num_matches = []
        for user in users:
            if username in user["username"]:
                num_matches.append(user)
                password = input(f"Enter password for {username}: ")
        if len(num_matches) == 0:
            print("This username does not exist. Please try again ")
            login.player(username)
        for i in num_matches:       # works bc there's only one dictionary in the list since only one username should match
            while i['password'] != password:
                print("incorrect password, try again")
                password = input(f"enter password for {username}: ")
        print("Congrats! You have successfully logged in ")
        # and then load that user's data or something idkidkidk
    def signup():
        create.add()
        

#login.signup()