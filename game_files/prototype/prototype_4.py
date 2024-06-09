import json
import os
import sys

sys.path.append("game_files")
from battle import *
from dialogues import *
from quest_and_rewards import *
from spaceship import *
from rand import *



class taiyo():
    def path(username):
        with open (r"game_files/classes/json/users.json", "r") as hi : 
            users = json.load(hi)

        with open (r"game_files/classes/json/entities.json", "r") as bye :
            entities = json.load(bye)
        dialogues_story.taiyo(0)
        rand.contin()
        dialogues_player.taiyo(0)
        rand.contin()
        x = 1
        while x <= 3:
            dialogues_story.taiyo(x)
            x += 1
            rand.contin()
        dialogues_player.taiyo(1)
        answer = input("")
        a = ['a','b']
        while answer not in a:
            print("You think it over before you speak and decide that it is not the right thing to say at the moment.")
            rand.contin()
            print("You try and think of another response.")
            dialogues_player.taiyo(1)
            a = input("").lower()
        rand.contin()
        dialogues_story.taiyo(4)
        rand.contin()
        dialogues_player.taiyo(2)
        rand.contin()
        x = 5
        while x <= 8:
            dialogues_story.taiyo(x)
            x += 1
            rand.contin()
        dialogues_player.taiyo(3)
        rand.contin()
        dialogues_story.taiyo(9)
        rand.contin()
        dialogues_story.taiyo(10)
        rand.contin()
        dialogues_player.taiyo(4)
        rand.contin()
        dialogues_player.taiyo(5)
        rand.contin()
        dialogues_story.taiyo(11)
        rand.contin()
        dialogues_story.taiyo(12)
        rand.contin()
        dialogues_player.taiyo(6)
        rand.contin()
        x = 13
        while x <= 15:
            dialogues_story.taiyo(x)
            x += 1
            rand.contin()
        dialogues_player.taiyo(7)
        rand.contin()
        dialogues_story.taiyo(19)       #stopped by guards here
        
        for user in users:
            if user['username'] == username:
                team_name = user['team']
        team = []
        for character in entities:
            if character['name'] in user['team']:
                team.append(character)
        a = []
        for character in team:
                a.append(character['hp'])
        ally_hp = sum(a)
        wave = 0
        y = 0
        z = team[y]   #first character in ally team
        l = len(team)    # number of team members - should be 4
        print("Battle 1:")
        while wave <= 2:
            quests.wave(wave,0)
            enemy_team = []       #list of the 3 trainee guards (whole dictionary)
            for enemy in entities:
                if enemy['name'] == "Trainee Guard":
                        for i in range(3):
                            enemy_team.append(enemy)
            rand.hp_full(enemy_team)
            b = []       # list of the 3 trainee guard' hps
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
                battle.cycle(z, enemy_team, team)
                b = []
                for en in enemy_team:
                    b.append(en['hp'])
                enemy_hp = sum(b)
                if enemy_hp <= 0:
                    break
                y += 1
                if y >= l:
                    y = 0
            if ally_hp <= 0:
                quests.lose(username, team)
                taiyo.path(username)
            else:
                for user in users:
                    reward = 7
                    add = user['crystals'] + reward
                    user['crystals'] = add
                    print(f"{username} now has {user['crystals']} crystals")
                new_file = "updated.json"
                with open(new_file, "w") as f:
                    json_string = json.dumps(users)
                    f.write(json_string)
                os.remove(r"game_files/classes/json/users.json")
                os.rename(new_file, r"game_files/classes/json/users.json")	
                print("You've gained 7 crystals.")
                rand.contin()
            wave += 1



        print("Battle 2:") 
        quests.wave(0,0)
        enemy_team = []       #list of the 3 trainee guards (whole dictionary)
        for enemy in entities:
            if enemy['name'] == "Trainee Guard":
                    for i in range(3):
                        enemy_team.append(enemy)
        rand.hp_full(enemy_team)
        b = []       # list of the 3 trainee guard' hps
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
            battle.cycle(z, enemy_team, team)
            b = []
            for en in enemy_team:
                b.append(en['hp'])
            enemy_hp = sum(b)
            if enemy_hp <= 0:
                break
            y += 1
            if y >= l:
                y = 0
        if ally_hp <= 0:
            quests.lose(username, team)
            taiyo.path(username)
        else:
            for user in users:
                reward = 7
                add = user['crystals'] + reward
                user['crystals'] = add
                print(f"{username} now has {user['crystals']} crystals")
            new_file = "updated.json"
            with open(new_file, "w") as f:
                json_string = json.dumps(users)
                f.write(json_string)
            os.remove(r"game_files/classes/json/users.json")
            os.rename(new_file, r"game_files/classes/json/users.json")	
            print("You've gained 7 crystals.")
            rand.contin()
        
        
        
        quests.wave(1,0)
        enemy_team = []       #list of the 4 guards (whole dictionary)
        for enemy in entities:
            if enemy['name'] == "Guard":
                    for i in range(4):
                        enemy_team.append(enemy)
        rand.hp_full(enemy_team)
        b = []       # list of the 3 trainee guard' hps
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
            battle.cycle(z, enemy_team, team)
            b = []
            for en in enemy_team:
                b.append(en['hp'])
            enemy_hp = sum(b)
            if enemy_hp <= 0:
                break
            y += 1
            if y >= l:
                y = 0
        if ally_hp <= 0:
            quests.lose(username, team)
            taiyo.path(username)
        else:
            for user in users:
                reward = 7
                add = user['crystals'] + reward
                user['crystals'] = add
                print(f"{username} now has {user['crystals']} crystals")
            new_file = "updated.json"
            with open(new_file, "w") as f:
                json_string = json.dumps(users)
                f.write(json_string)
            os.remove(r"game_files/classes/json/users.json")
            os.rename(new_file, r"game_files/classes/json/users.json")	
            print("You've gained 7 crystals.")
            rand.contin()
        
        quests.wave(1,1)
        enemy_team = []       #list of the 4 guards (whole dictionary)
        for enemy in entities:
            if enemy['name'] == "Guard Captain":
                    for i in range(4):
                        enemy_team.append(enemy)
        rand.hp_full(enemy_team)
        b = []       # list of the 3 trainee guard' hps
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
            battle.cycle(z, enemy_team, team)
            b = []
            for en in enemy_team:
                b.append(en['hp'])
            enemy_hp = sum(b)
            if enemy_hp <= 0:
                break
            y += 1
            if y >= l:
                y = 0
        if ally_hp <= 0:
            quests.lose(username, team)
            taiyo.path(username)
        else:
            for user in users:
                reward = 40
                add = user['crystals'] + reward
                user['crystals'] = add
                print(f"{username} now has {user['crystals']} crystals")
            new_file = "updated.json"
            with open(new_file, "w") as f:
                json_string = json.dumps(users)
                f.write(json_string)
            os.remove(r"game_files/classes/json/users.json")
            os.rename(new_file, r"game_files/classes/json/users.json")	
            print("You've gained 40 crystals.")
            rand.contin()
        

                # asahi arrives
        x = 20
        while x <= 22:
            dialogues_story.taiyo(x)
            x += 1
            rand.contin()
        dialogues_player.taiyo(8)
        answer = input("")
        a = ['a','b']
        while answer not in a:
            print("You think it over before you speak and decide that it is not the right thing to say at the moment.")
            rand.contin()
            print("You try and think of another response.")
            dialogues_player.taiyo(1)
            a = input("").lower()
        rand.contin()
        
        print("Battle 4: ")
        enemy_team = []       #list of the 4 guards (whole dictionary)
        for enemy in entities:
            if enemy['name'] == "Queen of Taiyo":
                    for i in range(4):
                        enemy_team.append(enemy)
        rand.hp_full(enemy_team)
        b = []       # list of the 3 trainee guard' hps
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
            battle.cycle(z, enemy_team, team)
            b = []
            for en in enemy_team:
                b.append(en['hp'])
            enemy_hp = sum(b)
            if enemy_hp <= 0:
                break
            y += 1
            if y >= l:
                y = 0
        if ally_hp <= 0:
            quests.lose(username, team)
            taiyo.path(username)
        else:
            for user in users:
                reward = 40
                add = user['crystals'] + reward
                user['crystals'] = add
                print(f"{username} now has {user['crystals']} crystals")
            new_file = "updated.json"
            with open(new_file, "w") as f:
                json_string = json.dumps(users)
                f.write(json_string)
            os.remove(r"game_files/classes/json/users.json")
            os.rename(new_file, r"game_files/classes/json/users.json")	
            print("You've gained 40 crystals.")
            rand.contin()


                # after all three taiyo battles...
        x = 23
        while x <= 25:
            dialogues_story.taiyo(x)
            x += 1
            rand.contin()
        print("[a] Pick it up")
        print("[b] Leave without it")
        answer = input("").lower()
        a = ['a','b']
        while answer not in a:
            answer = input("we know this is a hard choice...but YOU HAVE TO CHOOSE ONE").lower()
        if answer == "a":
            dialogues_story(26)
            rand.contin()
        elif answer == "b": 
            dialogues_story(27)
            rand.contin()
            dialogues_story(28)
            rand.contin()
        for user in users:
            if user['username'] == username:
                user['quest'].append('taiyo')
        new_file = "updated.json"
        with open(new_file, "w") as f:
            json_string = json.dumps(users)
            f.write(json_string)
        os.remove(r"game_files/classes/json/users.json")
        os.rename(new_file, r"game_files/classes/json/users.json")
                