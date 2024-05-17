""" import json
import os

with open (r"test.json", "r") as hi : 
    users = json.load(hi)

with open (r"game files\classes\json\entities.json", "r") as bye :
    entities = json.load(bye)

def select_character(username):             ## needs to be tested
        for user in users:
            if user['username'] == username:
                characters = user['character']
                team = user['team']
        a = 0
        b = ["A", "B", "C", "D"]
        print("You currently have this team setup:")
        for characters_team in team:
            print (f"[{b[a]}] {characters_team}")
            a += 1
        print("You currently have these characters:")
        for character in characters:
            print(character)
        answer = input("Would you like to change your team setup: y/n ").lower()
        while answer == "y":
            c = input("Choose the character to add onto team: ").title()
            d = input("Choose the character to replace(enter the letter in front of it): ").upper()
            a = 0
            for letter in b:
                if letter == d:
                    team[a] = c
                a += 1
            print (f"This is your new team set up: {team}")
            answer = input("continue changing team setup? y/n ").lower()
        if answer == "n":
            print(f"thank you for your time. You will now be returning to the space ship....")

select_character("examplee")

new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps(users)

    # Write the JSON string to the new JSON file
    f.write(json_string)

# Overwrite the old JSON file with the new one
os.remove(r"test.json")
os.rename(new_file, r"test.json")
 """

#import battle from battle.py and test it
import sys