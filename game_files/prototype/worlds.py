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
			dialogues_player.monde(0)
			a = input("").lower()
		rand.contin()
		dialogues_story.monde(3)
		rand.contin()
