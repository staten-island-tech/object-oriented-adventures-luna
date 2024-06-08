import json
import os
import sys

sys.path.append("game_files")
from rand import *
from dialogues import *
from battle import *
from quest_and_rewards import *


class prologue():
    def newbeginnings():
        x = 0
        for i in range(4):
            dialogues_story.prologue(x)
            x += 1
        rand.contin()
    def path(username):
        with open (r"game_files/classes/json/users.json", "r") as hi : 
            users = json.load(hi)

        with open (r"game_files/classes/json/entities.json", "r") as bye :
            entities = json.load(bye)
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
        l = len(team)
        y = []
        q = 0
        for i in range(l):
             y.append(q)
             q += 1
        print(team_name)
        print(team)
        q = 0
        z = team[y[q]]
        enemy_team = []
        for en in entities:
            if en['name'] == "Oblivion Guard":
                for i in range(3):
                    enemy_team.append(en)
        for enemy in enemy_team:
            b.append(enemy['hp'])
        enemy_hp = sum(b)
        while ally_hp >= 0 and enemy_hp >= 0:
            battle.attack_enemy(enemy_team, team)
            enemy_hp = sum(b)
            if enemy_hp <= 0:
                 break
            a = []
            for character in team:
                a.append(character['hp'])
            ally_hp = sum(a)
            if ally_hp <= 0:
                 break
            battle.cycle(z, enemy_team, team)
            b = []
            for en in enemy_team:
                b.append(en['hp'])
            q += 1
            if q > (l - 1):
                q = 0
            z = team[y[q]]
            rand.contin()
        if ally_hp <= 0:
            quests.lose(username, team)
            prologue.path(username)
        elif ally_hp == 0:
            quests.lose(username, team)
            prologue.path(username)
        else:
            print("you've won the battle!")
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
            os.remove(r"game_files/classes/json/users.json")
            os.rename(new_file, r"game_files/classes/json/users.json") 
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
        os.system("cls")
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
        wave = 0
        q = 0
        z = team[y[q]]
        while wave != 2:
            quests.wave(wave, 0)
            enemy_team = []
            for enemy in entities:
                if enemy['name'] == "Oblivion Guard":
                    for i in range(3):
                        enemy_team.append(enemy)
                elif enemy['name'] == "Oblivion Drones":
                    for i in range(2):
                        enemy_team.append(enemy)
            b = []
            for enemy in enemy_team:
                b.append(enemy['hp'])
            enemy_hp = sum(b)
            while ally_hp >= 0 and enemy_hp >= 0:
                battle.attack_enemy(enemy_team, team)
                a = []
                for character in team:
                    a.append(character['hp'])
                ally_hp = sum(a)
                if ally_hp <= 0:
                    break
                battle.cycle(z,enemy_team, team)
                b = []
                for en in enemy_team:
                    b.append(en['hp'])
                enemy_hp = sum(b)
                if enemy_hp <= 0:
                    break
                q += 1
                if q > (l - 1):
                    q = 0
            if ally_hp == 0:
                quests.lose(username, team)
                prologue.path(username)
            elif ally_hp < 0:
                quests.lose(username, team)
                prologue.path(username)
            else:
                print("You won the battle. You've gained 7 crystals")
                rewards = 7
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
                os.remove(r"game_files/classes/json/users.json")
                os.rename(new_file, r"game_files/classes/json/users.json") 
            wave += 1
            rand.contin()
        wave = 0
        quests.wave(wave, 0)
        enemy_team = []
        for enemy in entities:
            if enemy['name'] == "Oblivion Drones":
                for i in range(2):
                    enemy_team.append(enemy)
        b = []
        q = 0
        for enemy in enemy_team:
            b.append(enemy['hp'])
        enemy_hp = sum(b)
        while ally_hp >= 0 and enemy_hp >= 0:
                battle.attack_enemy(enemy_team, team)
                a = []
                for character in team:
                    a.append(character['hp'])
                ally_hp = sum(a)
                if ally_hp <= 0:
                     break
                battle.cycle(z,enemy_team, team)
                b = []
                for en in enemy_team:
                    b.append(en['hp'])
                enemy_hp = sum(b)
                if enemy_hp <= 0:
                     break
                q += 1
                if q > l - 1:
                    q = 0
        if ally_hp < 0:
                quests.lose(username, team)
                prologue.path(username)
        elif ally_hp == 0:
                quests.lose(username, team)
                prologue.path(username)
        else:
                print("you won the battle! You gained 7 crystals")
                rewards = 7
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
                os.remove(r"game_files/classes/json/users.json")
                os.rename(new_file, r"game_files/classes/json/users.json") 
        wave += 1
        quests.wave(wave, 1)
        enemy_team = []
        for enemy in entities:
            if enemy['name'] == "General Aeron":
                enemy_team.append(enemy)
        b = []
        for enemy in enemy_team:
            b.append(enemy['hp'])
        q = 0
        enemy_hp = sum(b)
        while ally_hp >= 0 and enemy_hp >= 0:
            battle.attack_enemy(enemy_team, team)
            a = []
            for character in team:
                a.append(character['hp'])
            ally_hp = sum(a)
            if ally_hp <= 0:
                 break
            battle.cycle(z,enemy_team, team)
            b = []
            for en in enemy_team:
                b.append(en['hp'])
            enemy_hp = sum(b)
            if enemy_hp <= 0:
                 break
            q += 1
            if q > (l - 1):
                    q = 0
        if ally_hp < 0:
                quests.lose(username, team)
                prologue.path(username)
        elif ally_hp == 0:
                quests.lose(username, team)
                prologue.path(username)
        elif enemy_hp <= 0:
                print("you won the battle! you gain 40 crystals")
                rewards = 40
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
                os.remove(r"game_files/classes/json/users.json")
                os.rename(new_file, r"game_files/classes/json/users.json")
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
        os.system("cls")
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
                dialogues_story.space_station(15)
                rand.contin()
                print("Great Job! You finished the first story quest!!")
        elif a == b[1]:
                dialogues_story.space_station(14)
                dialogues_story.space_station(15)
                rand.contin()
                print("Great Job! You finished the first story quest!!")
                print("Your Journey has ended...")
                print("You have not found your sibling, but you may continue playing to find out what would have happened if you chose the other route.")
        rewards = 1600
        for user in users:
            if user['username'] == username:
                    crystals = user['crystals']
                    add = crystals + rewards
                    print(f"{username} now has {add} crystals")
                    user['crystals'] = add
                    user['quest'].append("space station")
        new_file = "updated.json"
        with open(new_file, "w") as f:
                json_string = json.dumps(users)
                f.write(json_string)
        os.remove(r"game_files/classes/json/users.json")
        os.rename(new_file, r"game_files/classes/json/users.json")
        print("You've completed this mission. You've gained 1600 crystals")
        print("Going to spaceship...")
        rand.contin()
