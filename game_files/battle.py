import json
import os
import random
from rand import rand

with open (r"game_files/classes/json/users.json", "r") as hi : 
    users = json.load(hi)

with open (r"game_files/classes/json/entities.json", "r") as bye :
    entities = json.load(bye)


""" enemies = [{'name': "a", 
          'hp': 4500, 
          'attack': 40, 
          'type': "minion"}, 
          {'name': "b", 
           'hp': 10000, 
           'attack': 100, 
           'type': "boss"}] """
"""
characters = [{'name': "c", 
              'hp': 5000, 
              "rarity": "****", 
              'attack': [250, 750], 
              'element': "c1", 
              'weapon': "c2", 
              'type': "c3"}, 
              {'name': "d", 
               'hp': 5000, 
               "rarity": "****", 
               'attack': [250, 750], 
               'element': "d1", 
               'weapon': "d2", 
               'type': "d3"}]  """

class battle():
    def attack(x, y):                             # x is attack the enemy is taking (integer), y is list of dictionary of enemies, z is team you're using
        os.system("cls")
        for entity in entities:
            if entity['name'] == x:
                q = entity['attack'[0]]
        enemies = y
        for enemy in enemies:
            e = enemy['hp']
            enemy['hp'] = e - q
        for enemy in enemies: 
            print(f"Enemy Name: {enemy['name']}")
            print(f"HP: {enemy['hp']}")
    def ult(x, y):
        os.system("cls")
        for entity in entities:
            if entity['name'] == x:
                q = entity['attack'[1]]
        enemies = y
        for enemy in enemies:
            e = enemy['hp']
            enemy['hp'] = e - q
        for enemy in enemies:
            print(f"Enemy Name: {enemy['name']}")
            print(f"HP: {enemy['hp']}")
    def cycle(x, y, z):
        enemies = y
        characters = z
        for character in characters:
            if character == x:
                print (f"{character['name']} is preparing to attack.")
                print( )
                print(f"Name: {character['name']}")
                print(f"HP: {character['hp']}")
                global attack
                global name
                name = character['name']
                attack = character['attack']
                print(f"Attack: {attack[0]}")
                print(f"Ultimate: {attack[1]}")
                print( )
            continue
            
        for enemy in enemies:
            print (enemy['name'])
            print (enemy['hp'])
            print( )
        b = [7, 1, 3, 13, 9]
        c = random.randint(1, 20)
        e = 0
        if c in b:
            print("You are able to use your ultimate right now.")
            print("[U] Use Ultimate")
            e += 1
        else:
            print("You are not able to use your ultimate right now.")
        print("[A] Use attack")
        d = input("").upper()
        answers = ["U", "A"]
        if d not in answers:
            if e == 1:
                print("[U] Use Ultimate")
            print ("[A] Use attack")
            d = input("").upper()
        if d == "U":
            battle.ult(name, y)
        elif d == "A":
            battle.attack(name, y)
    def attack_enemy(y, z):
        enemies = y
        characters = z
        a = 0
        for enemy in enemies:
            a += 1
        b = a - 1
        c = random.randint(0, b)    #choose random enemy to attack
        a = 0
        for enemy in enemies:
            if a == c:
                d = enemy['name']
                attack_stat = enemy['attack']
            a += 1
        a = 0
        for character in characters:
            a += 1
        b = a - 1
        c = random.randint(0, b)
        a = 0
        for character in characters:
            if a == c:
                print(f"Enemy {d} is preparing to attack {character['name']}.")
                print(f"Your character has taken {attack_stat} damage.")
                print(f"Name: {character['name']}")
                new_hp = character['hp'] - attack_stat
                character['hp'] = new_hp
                print(f"HP: {new_hp}")
                rand.contin()
                os.system("cls")
            a += 1
    def select_character(username):             ## needs to be tested - TESTED 
        for user in users:
            if user['username'] == username:
                characters = user['characters']
                team = user['team']
        a = 0
        b = ["A", "B", "C", "D"]
        print("You currently have this team setup:")
        for characters_team in team:
            print (f"[{[b[a]]}] {characters_team}")
            a += 1
        print("You currently have these characters:")
        for character in characters:
            print(character)
        answer = input("Would you like to change your team setup: y/n ").lower()
        while answer == "y":
            c = input("Choose a character to add onto the team: ").title()
            e = []
            for entity in entities:
                e.append(entity['name'])
            while c not in e:
                print("This is not a character in the game! Please try again.")
                c = input("Choose a character to add onto the team: ").title()
            for charact in team:
                while charact == c:
                    print("You already have this character in the team! Please choose another character.")
                    c = input("Choose a character to add onto the team: ").title()
            for user in users:
                if user['username'] == username:
                    while c not in user['characters']:
                        print("You don't have this character in your data. Please try again.")
                        c = input("Choose a character to add onto the team: ").title()
            d = input("Choose the character to replace(enter the letter in front of it): ").upper()
            a = 0
            for letter in b:
                if letter == d:
                    team[a] = c
                a += 1
            print (f"This is your new team set up: {team}")
            answer = input("continue changing team setup? y/n ").lower()
        if answer == "n":
            print(f"Thank you for your time. You will now be returning to the space ship....")
        # append to json file
        new_file = "updated.json"
        with open(new_file, "w") as f:
            json_string = json.dumps(users)
            f.write(json_string)
        os.remove(r"game_files/classes/json/users.json")
        os.rename(new_file, r"game_files/classes/json/users.json")
