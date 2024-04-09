class user():
    def __init__(self, username, password, type):
        self.username = username
        self.passward = password
        self.type = type

class player(user):
    def __init__(self, username, password, type, version, team_lvl, crystals, stars):
        super().__init__(username, password, type)
        self.version = version
        self.team_lvl = team_lvl
        self.crystals = crystals
        self.stars = stars

class admin(user):
    def __init__(self, username, password, type, rank):
        super().__init__(username, password, type)
        self.rank = rank

def add():