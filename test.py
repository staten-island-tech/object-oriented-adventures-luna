
data = [{'username': 'a', 'password': 'abc'}]

def player():
        username = input("enter player username: ")
        password = input(f"enter password for {username}: ")
        for user in data:
            if username in user["username"] and password == user["password"]:
                print("Congrats! you are logged in")
                # and then load that player's data idk 
            else:
                print("invalid username or password. please try again")
                player()


""" def admin():
        username = input("enter admin username"): """
    

player()