
class Entities():                        # user does not inherit from entities class
    def __init__(self, name):
        self.name = name

class NPC(Entities):
    def __init__(self, name, mission, reward):
        super().__init__(name)
        self.mission = mission
        self.reward = reward

class Characters(Entities):              # MC is part of characters class
    def __init__(self, name, hp, attack, rarity, weapon, type, element):
        super().__init__(name)
        self.hp = hp
        self.attack = attack
        self.rarity = rarity
        self.weapon = weapon
        self.type = type
        self.element = element

class Enemies(Entities):
    def __init__(self, name, hp, attack):
        super().__init__(name)
        self.hp = hp
        self.attack = attack