import json
import sys
import os

from game_files.prototype.getting_in import *

with open (r"game_files\classes\json\users.json", "r") as hi : 
    users = json.load(hi)

with open (r"game_files\classes\json\entities.json", "r") as bye :
    entities = json.load(bye)

prototype.start()
prototype.start()   #for some reason it doesn't work with only one