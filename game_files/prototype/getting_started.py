import json
import os
import sys

sys.path.append("game_files")
from rand import random
from dialogues import *
from battle import *
from quest_and_rewards import *

with open (r"game_files\classes\json\users.json", "r") as hi : 
    users = json.load(hi)

with open (r"game_files\classes\json\entities.json", "r") as bye :
    entities = json.load(bye)

class prologue():
    def start(username):
        print("Pick your character: ")
        print("[A] Aelius")
        print("[B] Amaris")
        print("Please note that you will not be able to change your character once you have chosen the one you want.")
        a = input("").lower()
        b = ["a", "b"]
        while a not in b:
            print("Please choose again! That was not one of the options.")
            a = input("").lower()
        if a == b[0]:
            for user in users:
                if user['username'] == username:
                    c = user['characters']
                    c.append("Aelius")
                    d = user['team']
                    d.append("Aelius")
        elif a == b[1]:
            for user in users:
                if user['username'] == username:
                    c = user['characters']
                    c.append("Amaris")
                    d = user['team']
                    d.append("Aelius")
        new_file = "updated.json"
        with open(new_file, "w") as f:
            json_string = json.dumps(users)
            f.write(json_string)
        os.remove(r"game_files\classes\json\users.json")
        os.rename(new_file, r"game_files\classes\json\users.json")
        os.system("cls")
        print("Starting story now...")
        random.contin()
        random.load()
    def newbeginnings():
        x = 0
        for i in range(4):
            dialogues_story.prologue(x)
            x += 1
            random.contin()
        random.load()
    def path(username):
        x = 0
        for i in range(3):
            dialogues_story.space_station(x)
            x += 1
            random.contin()
        dialogues_player.space_station(0)
        random.contin()
        dialogues_story.space_station(3)
        random.contin()
        dialogues_player.space_station(1)
        random.contin()
        dialogues_story.space_station(4)
        random.contin()
        dialogues_player.space_station(2)
        random.contin()
        dialogues_story.space_station(5)
        random.contin()
        dialogues_player.space_station(3)
        random.contin()
        dialogues_story.space_station(6)
        random.contin()
        dialogues_player.space_station(4)
        random.contin()
        dialogues_story.space_station(7)
        random.contin()
        print("Before you begin this battle, you will first get someone to help you on this journey.")
        x = 0
        for i in range(2):
            dialogues_story.getting_asahi(x)
            x += 1
            random.contin()
        for user in users:
            if user['username'] == username:
                c = user['characters']
                c.append('Asahi')
                team_name = user['team']
                team_name.append('Asahi')
        new_file = "updated.json"
        with open(new_file, "w") as f:
            json_string = json.dumps(users)
            f.write(json_string)
        os.remove(r"game_files\classes\json\users.json")
        os.rename(new_file, r"game_files\classes\json\users.json")
        enemy_name = ["Oblivion Guard", "Oblivion Drone", "General Aeron"]
        enemy_team1 = []
        team = []
        for entity in entities:
            if entity['name'] in team_name:
                team.append(entity)
            elif entity['name'] in enemy_name:
                enemy_team1.append(entity)
        
        a = []
        b = []
        for character in team:
            a.append(character['hp'])
        for en in enemy_team:
            b.append(en['hp'])
        ally_hp = sum(a)
        enemy_hp = sum(b)
        y = 0
        l = len(team_name)
        enemy_team = []
        for en in enemy_team1:
            if en['name'] == "Oblivion Guards":
                for i in range(3):
                    enemy_team.append(en)
        while ally_hp != 0 and enemy_hp != 0:
            z = team_name[y]
            battle.cycle(z,enemy_team, team)
            b = []
            for en in enemy_team:
                b.append(en['hp'])
            battle.attack_enemy(enemy_team, team)
            a = []
            for character in team:
                a.append(character['hp'])
            ally_hp = sum(a)
            enemy_hp = sum(b)
            y += 1
            if y > l - 1:
                y = 0
        if ally_hp != 0:
            quests.lose(username, team)
            prologue.path(username)
        dialogues_story.space_station(8)
        random.contin()
        dialogues_player.space_station(5)
        answer = input("").lower()
        hi = ["a", "b"]
        while answer not in hi:
            print("You think it over before you speak and decide that it is not the right thing to say at the moment.")
            random.contin()
            print("You try and think of another response.")
            dialogues_player.space_station(5)
            answer = input("").lower()
        random.contin()
        dialogues_story.space_station(9)
        random.contin()
        dialogues_player.space_station(6)
        answer = input("").lower()
        hi = ["a", "b"]
        while answer not in hi:
            print("You think it over before you speak and decide that it is not the right thing to say at the moment.")
            random.contin()
            print("You try and think of another response.")
            dialogues_player.space_station(6)
            answer = input("").lower()
        random.contin()
        print("Getting ready for battle...")
