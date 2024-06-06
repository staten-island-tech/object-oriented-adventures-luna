import json
import os
import sys

sys.path.append("game_files")
from rand import *
from dialogues import *
from battle import *
from quest_and_rewards import *
from spaceship import *

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
                    user['characters'].append("Aelius")
                    user['team'].append("Aelius")
        elif a == b[1]:
            for user in users:
                if user['username'] == username:
                    user['characters'].append("Amaris")
                    user['team'].append("Amaris")
        new_file = "updated.json"
        with open(new_file, "w") as f:
            json_string = json.dumps(users)
            f.write(json_string)
        os.remove(r"game_files\classes\json\users.json")
        os.rename(new_file, r"game_files\classes\json\users.json")
        os.system("cls")
        print("Starting story now...")
        rand.contin()
        rand.load()
    def newbeginnings():
        x = 0
        for i in range(4):
            dialogues_story.prologue(x)
            x += 1
            rand.contin()
        rand.load()
    def path(username):
        x = 0
        for i in range(3):
            dialogues_story.space_station(x)
            x += 1
            rand.contin()
        dialogues_player.space_station(0)
        rand.contin()
        dialogues_story.space_station(3)
        rand.contin()
        dialogues_player.space_station(1)
        rand.contin()
        dialogues_story.space_station(4)
        rand.contin()
        dialogues_player.space_station(2)
        rand.contin()
        dialogues_story.space_station(5)
        rand.contin()
        dialogues_player.space_station(3)
        rand.contin()
        dialogues_story.space_station(6)
        rand.contin()
        dialogues_player.space_station(4)
        rand.contin()
        dialogues_story.space_station(7)
        rand.contin()
        print("Before you begin this battle, you will first get someone to help you on this journey.")
        x = 0
        for i in range(2):
            dialogues_story.getting_asahi(x)
            x += 1
            rand.contin()
        for user in users:
            if user['username'] == username:
                if 'Asahi' in user['character']:
                    pass
                else:
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
        team_name = []
        for user in users:
            if user['username'] == username:
                team_name = user['team']
        team = []
        for entity in entities:
            if entity['name'] in team_name:
                team.append(entity)
        a = []
        b = []
        for character in team:
            a.append(character['hp'])
        ally_hp = sum(a)
        enemy_hp = sum(b)
        y = 0
        z = team[y]
        l = len(team)
        enemy_team = []
        for enemy in entity:
            if enemy['name'] == "Oblivion Guard":
                for i in range(3):
                    enemy_team.append(en)
        for enemy in enemy_team:
            b.append(enemy['hp'])
        while ally_hp <= 0 and enemy_hp <= 0:
            battle.cycle(z, enemy_team, team)
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
        if ally_hp <= 0:
            quests.lose(username, team)
            prologue.path(username)
        rewards = 3
        for user in users:
            if user['username'] == username:
                crystals = user['crystals']
                add = crystals + rewards
                print(f"{username} now has {add} crystals")
                user['crystals'] = add
        new_file = "updated.json"
        with open(new_file, "w") as f:
            json_string = json.dumps(users)
            f.write(json_string)
        os.remove(r"game_files\classes\json\users.json")
        os.rename(new_file, r"game_files\classes\json\users.json") 
        print("You've gained 3 crystals")
        rand.contin()
        dialogues_story.space_station(8)
        rand.contin()
        dialogues_player.space_station(5)
        answer = input("").lower()
        hi = ["a", "b"]
        while answer not in hi:
            print("You think it over before you speak and decide that it is not the right thing to say at the moment.")
            rand.contin()
            print("You try and think of another response.")
            dialogues_player.space_station(5)
            answer = input("").lower()
        rand.contin()
        dialogues_story.space_station(9)
        rand.contin()
        dialogues_player.space_station(6)
        answer = input("").lower()
        hi = ["a", "b"]
        while answer not in hi:
            print("You think it over before you speak and decide that it is not the right thing to say at the moment.")
            rand.contin()
            print("You try and think of another response.")
            dialogues_player.space_station(6)
            answer = input("").lower()
        rand.contin()
        print("Getting ready for battle...")
        wave = 0
        z = team[y]
        y = 0
        while wave != 2:
            quests.wave(wave, 0)
            enemy_team = []
            for enemy in entity:
                if enemy['name'] == "Oblivion Guard":
                    for i in range(3):
                        enemy_team.append(en)
                elif enemy['name'] == "Oblivion Drones":
                    for i in range(2):
                        enemy_team.append(en)
            for enemy in enemy_team:
                b.append(enemy['hp'])
            while ally_hp <= 0 and enemy_hp <= 0:
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
                if ally_hp <= 0:
                    quests.lose(username, team)
                    prologue.path(username)
                else:
                    reward = 7
                    for user in users:
                        if user['username'] == username:
                            crystals = user['crystals']
                            add = crystals + rewards
                            print(f"{username} now has {add} crystals")
                            user['crystals'] = add
                    new_file = "updated.json"
                    with open(new_file, "w") as f:
                        json_string = json.dumps(users)
                        f.write(json_string)
                    os.remove(r"game_files\classes\json\users.json")
                    os.rename(new_file, r"game_files\classes\json\users.json") 
                    wave += 1
            print("You look around to see that there are no more monsters. As you let your guard down you see a shadow behind you.")
            rand.contin()
            wave = 0
            quests.wave(wave, 0)
            enemy_team = []
            for enemy in entity:
                if enemy['name'] == "Oblivion Drones":
                    for i in range(2):
                        enemy_team.append(en)
            for enemy in enemy_team:
                b.append(enemy['hp'])
            while ally_hp <= 0 and enemy_hp <= 0:
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
            if ally_hp <= 0:
                quests.lose(username, team)
                prologue.path(username)
            else:
                reward = 7
                for user in users:
                    if user['username'] == username:
                        crystals = user['crystals']
                        add = crystals + rewards
                        print(f"{username} now has {add} crystals")
                        user['crystals'] = add
                new_file = "updated.json"
                with open(new_file, "w") as f:
                    json_string = json.dumps(users)
                    f.write(json_string)
                os.remove(r"game_files\classes\json\users.json")
                os.rename(new_file, r"game_files\classes\json\users.json") 
            wave += 1
            quests.wave(wave, 1)
            enemy_team = []
            for enemy in entity:
                if enemy['name'] == "General Aeron":
                    enemy_team.append(en)
            for enemy in enemy_team:
                b.append(enemy['hp'])
            while ally_hp <= 0 and enemy_hp <= 0:
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
            if ally_hp <= 0:
                quests.lose(username, team)
                prologue.path(username)
            else:
                reward = 40
                for user in users:
                    if user['username'] == username:
                        crystals = user['crystals']
                        add = crystals + rewards
                        print(f"{username} now has {add} crystals")
                        user['crystals'] = add
                new_file = "updated.json"
                with open(new_file, "w") as f:
                    json_string = json.dumps(users)
                    f.write(json_string)
                os.remove(r"game_files\classes\json\users.json")
                os.rename(new_file, r"game_files\classes\json\users.json")
            rand.contin()
            dialogues_story.space_station(10)
            rand.contin()
            dialogues_player.space_station(7)
            rand.contin()
            a = input("").lower()
            b = ["a", "b"]
            while a not in b:
                print("You think it over before you speak and decide that it is not the right thing to say at the moment.")
                rand.contin()
                print("You try and think of another response.")
                dialogues_player.space_station(7)
                a = input("").lower()
            rand.contin()
            dialogues_story.space_station(11)
            rand.contin()
            dialogues_player.space_station(8)
            a = input("").lower()
            while a not in b:
                print("You think it over before you speak and decide that it is not the right thing to say at the moment.")
                rand.contin()
                print("You try and think of another response.")
                dialogues_player.space_station(8)
                a = input("").lower()
            rand.contin()
            dialogues_story.space_station(12)
            rand.contin()
            dialogues_player.space_station(9)
            a = input("").lower()
            while a not in b:
                print("You think it over before you speak and decide that it is not the right thing to say at the moment.")
                rand.contin()
                print("You try and think of another response.")
                dialogues_player.space_station(9)
                a = input("").lower()
                rand.contin()
            if a == b[0]:
                dialogues_story.space_station(13)
                rand.contin()
                dialogues_story.space_station(16)
                rand.contin()
                print("Great Job! You finished the first story quest!!")
            elif a == b[1]:
                dialogues_story.space_station(14)
                rand.contin()
                dialogues_story.space_station(15)
                rand.contin()
                print("Great Job! You finished the first story quest!!")
                print("Your Journey has ended...")
                print("You have not found your sibling, but you may continue playing to find out what would have happened if you chose the other route.")
            reward = 1600
            for user in users:
                if user['username'] == username:
                    crystals = user['crystals']
                    add = crystals + rewards
                    print(f"{username} now has {add} crystals")
                    user['crystals'] = add
            new_file = "updated.json"
            with open(new_file, "w") as f:
                json_string = json.dumps(users)
                f.write(json_string)
            os.remove(r"game_files\classes\json\users.json")
            os.rename(new_file, r"game_files\classes\json\users.json")
            rand.contin()
            print("Going to spaceship...")
            rand.load()
            spaceship.welcome(username)
prologue.path('exa')
