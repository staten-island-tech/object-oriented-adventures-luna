enemies = [{'name': "a", 
          'hp': 4500, 
          'attack': 40, 
          'type': "minion"}, 
          {'name': "b", 
           'hp': 10000, 
           'attack': 100, 
           'type': "boss"}]

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
               'type': "d3"}]

class battle():
    def attack(x):
        print("Choose an enemy to attack:")
        a = 0
        b = ["A", "B", "C", "D", "E", "F"]
        for enemy in enemies: 
            print(f"[{b[a]}] {enemy['name']}")
            print(f"HP: {enemy['hp']}")
            a += 1 
        enemy_chosen = input("").upper()
        c = 0
        d = b[c]
        while d != enemy_chosen:
            c += 1
            d = b[c]
        a = 0
        for enemy in enemies:
            if a == c:
                e = enemy['hp']
                f = e
                d = x
                enemy['hp'] = f - d
            a += 1
        for enemy in enemies: 
            print(f"Enemy Name: {enemy['name']}")
            print(f"HP: {enemy['hp']}")
    def ult(x):
        for enemy in enemies:
            e = enemy['hp']
            f = e
            d = x
            enemy['hp'] = f - d
        for enemy in enemies: 
            print(f"Enemy Name: {enemy['name']}")
            print(f"HP: {enemy['hp']}")
    def cycle(x):
        a = 0
        import random
        for character in characters:
            if a == x:
                print(f"Name: {character['name']}")
                print(f"HP: {character['hp']}")
                print(f"Attack: {character['attack'[0]]}")
                attack_stat = character['attack']
        for enemy in enemies:
            print (enemy['name'])
            print (enemy['hp'])
        b = 7
        c = random.randrange(1, 20)
        if c == b:
            print("You are able to use your ult right now. It will affect all enemies")
            print(f"Ult: {attack_stat[1]}")
            print("[U] Use Ultimate")
        print("[A] Use attack")
        d = input("").upper()
        answers = ["U", "A"]
        if d not in answers:
            print("[U] Use Ultimate")
            print("[A] Use attack")
        if d == "U":
            battle.ult(attack_stat[1])
        elif d == "A":
            battle.attack(attack_stat[0])
    def attack_enemy(x):
        import random
        a = 0
        for enemy in enemies:
            a += 1
        b = a - 1
        c = random.randrange(0, b)
        a = 0
        for enemy in enemy:
            if a == c:
                d = enemy['name']
                print(f"Enemy {enemy['name']} is preparing to attack.")
                attack_stat = enemy['attack']
            a += 1
        a = 0
        for character in characters:
            a += 1
        b = a - 1
        c = random.randrange(0, b)
        a = 0
        for character in characters:
            if a == c:
                print(f"Enemy {d} is preparing to attack {character['name']}.")
    def hp():
        pass

battle.attack(250)