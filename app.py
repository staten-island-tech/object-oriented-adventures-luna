import json

from game_files.prototype.getting_in import *

data_users = open("./game_files/classes/json/users.json", encoding="utf8")
users = json.load(data_users)

data_entities = open("./game_files/classes/json/entities.json", encoding="utf8")
entities = json.load(data_entities)

prototype.start()
prototype.start()   #for some reason it doesn't work with only one