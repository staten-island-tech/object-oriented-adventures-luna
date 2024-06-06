import json
import os
import sys

sys.path.append("game_files")
from battle import *
from dialogues import *
from quest_and_rewards import *
from rand import *

with open (r"game_files\classes\json\users.json", "r") as hi : 
    users = json.load(hi)

with open (r"game_files\classes\json\entities.json", "r") as bye :
    entities = json.load(bye)

class worlds():
	def monde_mission(username):
		dialogues_story.monde(0)
		rand.contin()
		dialogues_player.monde(0)
		a = input("").lower()
		b = ["a", "b"]
		while a not in b:
			print("You think it over before you speak and decide that it is not the right thing to say at the moment.")
			rand.contin()
			print("You try and think of another response.")
			dialogues_player.monde(0)
			a = input("").lower()
		rand.contin()
		dialogues_story.monde(1)
		rand.contin()
		dialogues_story.monde(2)
		rand.contin()
		dialogues_player.monde(1)
		a = input("").lower()
		while a not in b:
			print("You think it over before you speak and decide that it is not the right thing to say at the moment.")
			rand.contin()
			print("You try and think of another response.")
			dialogues_player.monde(1)
			a = input("").lower()
		rand.contin()
		dialogues_story.monde(3)
		rand.contin()
		dialogues_player.monde(2)
		rand.contin()
		dialogues_story.monde(4)
		rand.contin()
		dialogues_player.monde(3)
		rand.contin()
		dialogues_story.monde(5)
		rand.contin()
		dialogues_player.monde(4)
		rand.contin()
		x = 6
		for i in range(3):		## x6 to x8
			dialogues_story.monde(x)
			rand.contin()
			x += 1
		dialogues_player.monde(5)
		rand.contin()
		dialogues_story.monde(9)
		rand.contin()
		dialogues_player.monde(6)
		a = input("").lower()
		while a not in b:
			print("You think it over before you speak and decide that it is not the right thing to say at the moment.")
			rand.contin()
			print("You try and think of another response.")
			dialogues_player.monde(6)
			a = input("").lower()
		rand.contin()
		team_name = []
		for user in users:
			if user['username'] == username:
				team_name = user['team']
		team = []
		for entity in entities:
			if entity['name'] in team:
				team.append(entity)
		a = []
		for character in team:
			a.append(character['hp'])
		ally_hp = sum(a)
		wave = 0
		print("Battle 1: ")
		while wave != 2:
			quests.wave(wave, 0)
			enemy_team = []
			for enemy in entities:
				if enemy['name'] == "Hydro Robot":
					for i in range(3):
						enemy_team.append(enemy)
			b = []
			for en in enemy_team:
				b.append(en['hp'])
			enemy_hp = sum(b)
			y = 0
			z = team[y]
			l = len(team)
			while ally_hp >= 0 or enemy_hp >= 0:
				battle.cycle(z, enemy_team, team)
				b = []
				for en in enemy_team:
					b.append(en['hp'])
				battle.attack_enemy(enemy_team, team)
				a = []
				for character in team:
					a.append(character['hp']
				ally_hp = sum(a)
				enemy_hp = sum(b)
				y += 1
				if y >= l:
					y = 0
			if ally_hp <= 0:
				quests.lose(username, team)
				worlds.monde_mission(username)
			rewards = 7
			for user in users:
				if user['username'] == username:
					crystals = user['crystals']
					add = crystals + rewards
					print(f"{username} now has {add} crystals.")
					user['crystals'] = add
			new_file = "updated.json"
			with open(new_file, "w") as f:
				json_string = json.dumps(users)
				f.write(json_string)
			os.remove(r"game_files\classes\json\users.json")
			os.rename(new_file, r"game_files\classes\json\users.json")
			print("You've gained 7 crystals")
			wave += 1
		print("Battle 2")
		while wave != 2:
			quests.wave(wave, 0)
			enemy_team = []
			for enemy in entities:
				if enemy['name'] == "Hydro Robot Dog":
					for i in range(3):
						enemy_team.append(enemy)
			b = []
			for en in enemy_team:
				b.append(en['hp'])
			enemy_hp = sum(b)
			y = 0
			while ally_hp >= 0 or enemy_hp >= 0:
				battle.cycle(z, enemy_team, team)
				b = []
				for en in enemy_team:
					b.append(en['hp'])
				battle.attack_enemy(enemy_team, team)
				a = []
				for character in team:
					a.append(character['hp']
				ally_hp = sum(a)
				enemy_hp = sum(b)
				y += 1
				if y >= l:
					y = 0
			if ally_hp <= 0:
				quests.lose(username, team)
				worlds.monde_mission(username)
			rewards = 7
			for user in users:
				if user['username'] == username:
					crystals = user['crystals']
					add = crystals + rewards
					print(f"{username} now has {add} crystals.")
					user['crystals'] = add
			new_file = "updated.json"
			with open(new_file, "w") as f:
				json_string = json.dumps(users)
				f.write(json_string)
			os.remove(r"game_files\classes\json\users.json")
			os.rename(new_file, r"game_files\classes\json\users.json")
			print("You've gained 7 crystals")
			wave += 1
		rand.contin()
		print("Battle 3")
		quests.wave(0,0)
		enemy_team = []
		for enemy in entities:
			if enemy['name'] == "Hydro Robot":
				enemy_team.append(enemy)
			elif enemy['name'] == "Hydro Robot Dog':
				enemy_team.append(enemy)
		b = []
		for en in enemy_team:
			b.append(en['hp'])
		enemy_hp = sum(b)
		y = 0
		while ally_hp >= 0 or enemy_hp >= 0:
			battle.cycle(z, enemy_team, team)
			b = []
			for en in enemy_team:
				b.append(en['hp'])
			battle.attack_enemy(enemy_team, team)
			a = []
			for character in team:
				a.append(character['hp']
			ally_hp = sum(a)
			enemy_hp = sum(b)
			y += 1
			if y >= l:
				y = 0
		if ally_hp <= 0:
			quests.lose(username, team)
			worlds.monde_mission(username)
		rewards = 7
		for user in users:
			if user['username'] == username:
				crystals = user['crystals']
				add = crystals + rewards
				print(f"{username} now has {add} crystals.")
				user['crystals'] = add
		new_file = "updated.json"
		with open(new_file, "w") as f:
			json_string = json.dumps(users)
			f.write(json_string)
		os.remove(r"game_files\classes\json\users.json")
		os.rename(new_file, r"game_files\classes\json\users.json")
		print("You've gained 7 crystals")
		rand.contin()
		quests.wave(1,1)
		enemy_team = []
		for enemy in entities:
			if enemy['name'] == "Giant Hydro Robot":
				enemy_team.append(enemy)
		b = []
		for en in enemy_team:
			b.append(en['hp'])
		enemy_hp = sum(b)
		y = 0
		while ally_hp >= 0 or enemy_hp >= 0:
			battle.cycle(z, enemy_team, team)
			b = []
			for en in enemy_team:
				b.append(en['hp'])
			battle.attack_enemy(enemy_team, team)
			a = []
			for character in team:
				a.append(character['hp']
			ally_hp = sum(a)
			enemy_hp = sum(b)
			y += 1
			if y >= l:
				y = 0
		if ally_hp <= 0:
			quests.lose(username, team)
			worlds.monde_mission(username)
		rewards = 40
		for user in users:
			if user['username'] == username:
				crystals = user['crystals']
				add = crystals + rewards
				print(f"{username} now has {add} crystals.")
				user['crystals'] = add
		new_file = "updated.json"
		with open(new_file, "w") as f:
			json_string = json.dumps(users)
			f.write(json_string)
		os.remove(r"game_files\classes\json\users.json")
		os.rename(new_file, r"game_files\classes\json\users.json")
		print("You've gained 40 crystals")
		rand.contin()
		dialogues_story.monde(10)
		rand.contin()
		dialogues_player.monde(7)
		rand.contin()
		dialogues_story.monde(11)
		rand.contin()
		dialogues_player.monde(8)
		a = input("").lower()
		while a not in b:
			print("You think it over before you speak and decide that it is not the right thing to say at the moment.")
			rand.contin()
			print("You try and think of another response.")
			dialogues_player.monde(8)
			a = input("").lower()
		rand.contin()
		dialogues_story.monde(12)
		rand.contin()
		dialogues_player.monde(9)
		rand.contin()
		dialogues_story.monde(13)
		rand.contin()
		dialogues_story.monde(14)
		rand.contin()
		dialogues_player.monde(10)
		rand.contin()
		dialogues_story.monde(15)
		rand.contin()
		dialogues_player.monde(11)
		rand.contin()
		dialogues_story.monde(16)
		rand.contin()
		dialogues_player.monde(12)
		rand.contin()
		dialogues_story.monde(17)
		rand.contin()
		dialogues_player.monde(13)
		rand.contin()
		dialogues_story.monde(18)
		rand.contin()
		print("Going back to spaceship...")
		rand.contin()
		rand.load()
