
#import stuff


users = [
    {
        'username': "example",
        "password": "123",
        "type": "player",
        "version": 0,
        "team_lvl": 1,
        'crystals': 500,
        "stars": 0,
        "character": []
    },
    {
        "username": "examplee",
        "password": "abc",
        "type": "player",
        "version": 0,
        "team_lvl": 1,
        "crystals": 200,
        "stars": 0,
        "character": []
    },
    {
        "username": "exampleee",
        "password": "abc",
        "type": "player",
        "version": 0,
        "team_lvl": 1,
        "crystals": 0,
        "stars": 0,
        "character": []
    }
]

star_counter = 0

class star():
    
    def soft_pity():
        while star_counter == 70:
            pass
            #increase

    def pull_one(usernam):
        a = 0
        for user in users:
            while user['username'] != usernam:
               a += 1
            crystals = user['crystals']
            print(f"{usernam} currently has {crystals} crystals")
            break
        crystals -= 160
        print(f"{usernam} now has {crystals} crystals left")
        
         #subtract 160 crystals from user - DONE
        #if not enough, go to do mission
        #choose random character, use rates
        # check for dupes: if yes, add 80 crystals
        # if no, append character to user data

        

    def pull_ten(user):
        # subtract 1600 crystals
        #if not enough, go to do mission
        #choose random character 10 times using while loop or something
        #check for dupe each time: if yes add 80 crystals
        #if no append to user data
        pass

star.pull_one("example")
