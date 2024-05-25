with open (r"game_files\classes\json\users.json", "r") as hi : 
    users = json.load(hi)

class spaceship():
    def welcome():
        print("??: Welcome abroad the spaceship! Captain Xingxing, here!")
        c = input("[A] Continue").upper()
            while c != "A":
                c = input("").upper()
        print("Xingxing: Greetings! Is there anything you would like?")
        
    def quest(username):
        for user in users:
            if user['name'] == username:
                quests = len(user['quest'])
        worlds = ["spaceship", "pero", "monde", "taiyo"]
        
    def star_system():
        pass
    def team():
        pass
