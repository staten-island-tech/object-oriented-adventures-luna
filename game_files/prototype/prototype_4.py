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
        while x < 3:
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
        while x < 8:
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
        while x < 15:
            dialogues_story(x)
            x += 1
            rand.contin()
        dialogues_player.taiyo(7)
        rand.contin()
        x = 16
        while x < 22:
            dialogues_story(x)
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
        

