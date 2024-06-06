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

class worlds():
  def pero_mission(username):
