
class Entities():                        # user does not inherit from entities class
    def __init__(self, name):
        self.name = name


class NPC(Entities):
    def __init__(self, name):
        super().__init__(name)

class Characters(Entities):               # MC is part of characters class
    def __init__(self, name):
        super().__init__(name)



class Enemies():
    def __init__(self, name):
        self.name = name


class Stars():
    def djslfkajds;fjaw