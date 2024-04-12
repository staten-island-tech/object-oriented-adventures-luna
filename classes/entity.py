import json
import os


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


with open("entities.json", "r") as f:
    data = json.load(f)

    def add():
        a = input("Would you like to add an entity? y/n ").lower()
        while a != "y" or a != "n":
            a = input("Would you like to add an entity? y/n ").lower()
        while a != "y":
            type_entity = input("What type of entity would you like to make? (npc, character, enemy) ").lower()
            type_entity_list = ["character", "enemy", "npc"]
            while type_entity not in type_entity_list:
                type_entity = input("What type of entity would you like to make? (npc, character, enemy) ").lower()
            if type_entity == "character":
                name = input("What is the character's name? ").title()
                entities = open("./entities.json", encoding="utf8")
                entities_data = json.load(entities)
                for entity in entities_data:
                    while name == entity["name"]:
                        print(f"{name} has already been used.")
                        name = input("What is another name for the character? ").title()
                hp_beta = 1000
                attack_beta = 250
                rarity = input("What rarity would the character be? (**** or *****) ")
                rarity_list = ["****", "*****"]
                while rarity not in rarity_list:
                    rarity = input("What rarity would the character be? (**** or *****) ")
                if rarity == "****":
                    hp = hp_beta * 4
                    attack = attack_beta * 4
                elif rarity == "*****":
                    hp = hp_beta * 7.5
                    attack = attack_beta * 7.5
                weapon = input(f"Pick a weapon for {name}: ").lower()
                type_list = ["hunt", "destruction", "nihility", "preservation", "erudition", "harmony", "abundance"]
                type = input(f"Pick a type: ({type_list}) ").lower()
                while type not in type_list:
                    type = input(f"Pick a type: ({type_list}) ").lower()
                element_list = ["quantum", "imaginary", "fire", "ice", "wind", "physical", "water", "lightning"]
                element = input(f"Pick an element: ({element_list}) ").lower()
                while element not in element_list:
                    element = input(f"Pick an element: ({element_list}) ").lower()
                character_made = Characters(name, hp, attack, rarity, weapon, type, element)
                print(character_made.__dict__)
                data.append(character_made.__dict__)
            if type_entity == "npc":
                name = input("What is the npc's name? ").title()
                entities = open("./entities.json", encoding="utf8")
                entities_data = json.load(entities)
                for entity in entities_data:
                    while name == entity["name"]:
                        print(f"{name} has already been used.")
                        name = input("What is another name for the npc? ").title()
                mission_beta = input("Put in a world name: ").title()
                world_list = ["Monde", "Pero", "Taiyo"]
                while mission_beta not in world_list:
                    mission_beta = input("Put in a world name: ").title()
                



new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps(data)

    # Write the JSON string to the new JSON file
    f.write(json_string)

# Overwrite the old JSON file with the new one
os.remove("entities.json")
os.rename(new_file, "entities.json")