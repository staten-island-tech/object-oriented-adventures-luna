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

class battle_character():
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
    def cycle():
        pass
    def hp():
        pass

class battle_enemy():
    pass

battle_character.ult(500)