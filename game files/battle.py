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
    def attack():
        print("Choose an enemy to attack:")
        a = 0
        b = ["A", "B", "C", "D", "E", "F"]
        for enemy in enemies: 
            print(f"[{b[a]}] {enemy['name']}")
            a += 1 
        enemy_chosen = input("").upper()
        c = 0
        d = b[c]
        while d != enemy_chosen:
            c += 1
        
    def ult():
        pass
    def cycle():
        pass
    def hp():
        pass

class battle_enemy():
    pass

battle_character.attack()