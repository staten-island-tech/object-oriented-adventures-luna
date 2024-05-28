
#import battle.py from game_files and test it - TESTED   importing works :D
""" import sys
sys.path.append('/game_files')
from game_files import battle
battle.battle.select_character("exa") """

team = [{
                "name": "Amaris",
                "hp": 0,
                "attack": [
                    500,
                    1500
                ],
                "rarity": "*****",
                "weapon": "stellar gun",
                "type": "destruction",
                "element": "quantum"
            },
            {
                "name": "Aelius",
                "hp": 0,
                "attack": [
                    500,
                    1500
                ],
                "rarity": "*****",
                "weapon": "stellar gun",
                "type": "destruction",
                "element": "imaginary"
            },
            {"name": "",
                "hp": 0,
                "attack": [],
                "rarity": "",
                "weapon": "",
                "type": "",
                "element": ""},
            {"name": "",
                "hp": 0,
                "attack": [],
                "rarity": "",
                "weapon": "",
                "type": "",
                "element": ""}
        ]


def lose(username):
    a = 0
    for character in team:
        if character["hp"] == 0:        # 
            a += 1
    if a == 4:
        print(f"{username}, you have lost this battle. You will now be transported back to the spaceship for further treatment.")
    
lose("ex")