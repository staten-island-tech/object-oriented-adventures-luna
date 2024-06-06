import json
import os
import sys

sys.path.append("game_files")
from battle import *
from dialogues import *
from quest_and_rewards import *
from spaceship import *
from rand import *

with open (r"game_files\classes\json\users.json", "r") as hi : 
    users = json.load(hi)

with open (r"game_files\classes\json\entities.json", "r") as bye :
    entities = json.load(bye)

class taiyo():
    def path(username):
        dialogues_story.taiyo(0)
        rand.contin()
        dialogues_player.taiyo(0)
        rand.contin()
        x = 1
        while x != 3:
            dialogues_story(x)
            x += 1
            rand.contin()
        dialogues_player.taiyo(1)
        answer = input("")
        a = ['a','b']
        while answer not in a:
            dialogues_story.taiyo(3)
            dialogues_player.taiyo(1)
            answer = input("")
        rand.contin()
        dialogues_story.taiyo(4)
        rand.contin()
        dialogues_player.taiyo(2)
        rand.contin()
        x = 5
        while x != 8:
            dialogues_story(x)
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
        while x != 15:
            dialogues_story(x)
            x += 1
            rand.contin()
        dialogues_player.taiyo(7)
        rand.contin()
        dialogues_story.taiyo(19)       #stopped by guards here
        
        for user in users:
            if user['username'] == username:
                team = []
                for character in entities:
                    if character['name'] in user['team']:
                        team.append(character)
                    else:
                        pass
                team_hps = []
                for team_member in team:
                    team_hps.append(team_member['hp'])
                total_ally_hp = sum(team_hps)
                print("Getting ready for battle...")
                wave = 0
                y = 0
                z = team[y]   #first character in ally team
                l = len(team)    # number of team members - should be 4
                while wave < 2:
                    quests.wave(wave,0)
                    enemy_team = []       #list of the 3 trainee guards (whole dictionary)
                    for enemy in entities:
                        if enemy['name'] == "Trainee Guard":
                            x = 1
                            while x != 3:
                                enemy_team.append(enemy)
                                x += 1
                    enemy_hps = []       # list of the 3 trainee guard' hps
                    for i in enemy_team:
                        enemy_hps.append(i['hp'])
                    total_enemy_hp = sum(enemy_hps)       #sum of the 3 trainee guard hps
                
                    while total_ally_hp <= 0 and total_enemy_hp <= 0:
                        battle.cycle(z, enemy_team, team)
                        enemy_hps = []
                        for i in enemy_team:
                            enemy_hps.append(i['hp'])
                        battle.attack_enemy(enemy_team, team)
                        team_hps = []
                        for character in team:
                            team_hps.append(character['hp'])
                        total_ally_hp = sum(team_hps)
                        total_enemy_hp = sum(enemy_hps)
                        y += 1
                        if y > (l - 1):
                            y = 0
                        if total_ally_hp <= 0:
                            quests.lose(username, team)
                            taiyo.path(username)
                        else:
                            reward = 7
                            add = user['crystals'] + reward
                            user['crystals'] = add
                            print(f"{username} now has {user['crystals']} crystals")
                        new_file = "updated.json"
                        with open(new_file, "w") as f:
                            json.dump(users, f)
                        os.remove(r"game_files\classes\json\users.json")
                        os.rename(new_file, r"game_files\classes\json\users.json")
                    wave += 1
                    rand.contin()
                
                #second battle wave 1
                wave = 0
                quests.wave(wave,1)
                enemy_team = []       #list of the 3 trainee guards (whole dictionary)
                for enemy in entities:
                    if enemy['name'] == "Trainee Guard":
                        x = 1
                        while x != 3:
                            enemy_team.append(enemy)
                            x += 1
                enemy_hps = []       # list of the 3 trainee guard' hps
                for i in enemy_team:
                    enemy_hps.append(i['hp'])
                total_enemy_hp = sum(enemy_hps)       #sum of the 3 trainee guard hps
                
                while total_ally_hp <= 0 and total_enemy_hp <= 0:
                    battle.cycle(z, enemy_team, team)
                    enemy_hps = []
                    for i in enemy_team:
                        enemy_hps.append(i['hp'])
                    battle.attack_enemy(enemy_team, team)
                    team_hps = []
                    for character in team:
                        team_hps.append(character['hp'])
                    total_ally_hp = sum(team_hps)
                    total_enemy_hp = sum(enemy_hps)
                    y += 1
                    if y > (l - 1):
                        y = 0
                if total_ally_hp <= 0:
                    quests.lose(username, team)
                    taiyo.path(username)
                else:
                    reward = 40       
                    add = user['crystals'] + reward
                    user['crystals'] = add
                    print(f"{username} now has {user['crystals']} crystals")
                new_file = "updated.json"
                with open(new_file, "w") as f:
                    json.dump(users, f)
                os.remove(r"game_files\classes\json\users.json")
                os.rename(new_file, r"game_files\classes\json\users.json")
        
                rand.contin()

                    #second wave of second taiyo battle (4 normal guards)
                wave += 1    # wave = 2
                quests.wave(wave, 1)
                enemy_team = []       
                for enemy in entities:
                    if enemy['name'] == "Guard":
                        x = 1
                        while x != 4:
                            enemy_team.append(enemy)
                            x += 1
                enemy_hps = []      
                for i in enemy_team:
                    enemy_hps.append(i['hp'])
                total_enemy_hp = sum(enemy_hps)       
                
                while total_ally_hp <= 0 and total_enemy_hp <= 0:
                    battle.cycle(z, enemy_team, team)
                    enemy_hps = []
                    for i in enemy_team:
                        enemy_hps.append(i['hp'])
                    battle.attack_enemy(enemy_team, team)
                    team_hps = []
                    for character in team:
                        team_hps.append(character['hp'])
                    total_ally_hp = sum(team_hps)
                    total_enemy_hp = sum(enemy_hps)
                    y += 1
                    if y > (l - 1):
                        y = 0
                if total_ally_hp <= 0:
                    quests.lose(username, team)
                    taiyo.path(username)
                else:
                    reward = 40       
                    add = user['crystals'] + reward
                    user['crystals'] = add
                    print(f"{username} now has {user['crystals']} crystals")
                new_file = "updated.json"
                with open(new_file, "w") as f:
                        json.dump(users, f)
                os.remove(r"game_files\classes\json\users.json")
                os.rename(new_file, r"game_files\classes\json\users.json")
        
                rand.contin()

                # second battle wave 3 (Captain of the Guard)
                wave += 1    # wave = 3
                quests.wave(wave, 1)
                enemy_team = []       
                for enemy in entities:
                    if enemy['name'] == "Guard Captain":
                        enemy_team.append(enemy)
                enemy_hps = []      
                for i in enemy_team:
                    enemy_hps.append(i['hp'])
                total_enemy_hp = sum(enemy_hps)       
                
                while total_ally_hp <= 0 and total_enemy_hp <= 0:
                    battle.cycle(z, enemy_team, team)
                    enemy_hps = []
                    for i in enemy_team:
                        enemy_hps.append(i['hp'])
                    battle.attack_enemy(enemy_team, team)
                    team_hps = []
                    for character in team:
                        team_hps.append(character['hp'])
                    total_ally_hp = sum(team_hps)
                    total_enemy_hp = sum(enemy_hps)
                    y += 1
                    if y > (l - 1):
                        y = 0
                if total_ally_hp <= 0:
                    quests.lose(username, team)
                    taiyo.path(username)
                else:
                    reward = 40       
                    add = user['crystals'] + reward
                    user['crystals'] = add
                    print(f"{username} now has {user['crystals']} crystals")
                new_file = "updated.json"
                with open(new_file, "w") as f:
                        json.dump(users, f)
                os.remove(r"game_files\classes\json\users.json")
                os.rename(new_file, r"game_files\classes\json\users.json")
        
                rand.contin()

                # asahi arrives
                x = 20
                while x != 22:
                    dialogues_story.taiyo(x)
                    x += 1
                    rand.contin()
                dialogues_player.taiyo(8)
                answer = input("")
                a = ['a','b']
                while answer not in a:
                    dialogues_story.taiyo(22)
                    dialogues_player.taiyo(8)
                    answer = input("")
                rand.contin()

                # third battle wave 1
                wave = 0    
                quests.wave(wave, 1)
                enemy_team = []       
                for enemy in entities:
                    if enemy['name'] == "Queen of Taiyo":
                        enemy_team.append(enemy)
                enemy_hps = []      
                for i in enemy_team:
                    enemy_hps.append(i['hp'])
                total_enemy_hp = sum(enemy_hps)       
                
                while total_ally_hp <= 0 and total_enemy_hp <= 0:
                    battle.cycle(z, enemy_team, team)
                    enemy_hps = []
                    for i in enemy_team:
                        enemy_hps.append(i['hp'])
                    battle.attack_enemy(enemy_team, team)
                    team_hps = []
                    for character in team:
                        team_hps.append(character['hp'])
                    total_ally_hp = sum(team_hps)
                    total_enemy_hp = sum(enemy_hps)
                    y += 1
                    if y > (l - 1):
                        y = 0
                if total_ally_hp <= 0:
                    quests.lose(username, team)
                    taiyo.path(username)
                else:
                    reward = 40       
                    add = user['crystals'] + reward
                    user['crystals'] = add
                    print(f"{username} now has {user['crystals']} crystals")
                new_file = "updated.json"
                with open(new_file, "w") as f:
                        json.dump(users, f)
                os.remove(r"game_files\classes\json\users.json")
                os.rename(new_file, r"game_files\classes\json\users.json")
        
                rand.contin()

                # after all three taiyo battles...
                x = 23
                while x != 25:
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
                else: 
                    dialogues_story(27)
                    rand.contin()
                    dialogues_story(28)


                
                
                




        

