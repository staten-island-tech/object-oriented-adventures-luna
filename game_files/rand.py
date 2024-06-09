import os
import json

with open (r"game_files/classes/json/entities.json", "r") as bye :
    entities = json.load(bye)

class rand():
  def contin():
    print("[A] Continue")
    c = input("").upper()
    while c != "A":
      print("That is not one of the answer choices please choose again!")
      c = input("").upper()
    os.system("cls")
  def quest_selector(username):
    print("[S] Story Quest")
  def hp_full(x):
    enemy_team = x
    for enemy in enemy_team:
      if enemy['hp'] == 0:
        if enemy['type'] == "minion":
          enemy['hp'] = 4500
        elif enemy['name'] == "Queen of Taiyo":
          enemy['hp'] = 20000
        elif enemy['type'] == "boss":
          enemy['hp'] = 10000
      elif enemy['hp'] < 0:
        if enemy['type'] == "minion":
          enemy['hp'] = 4500
        elif enemy['name'] == "Queen of Taiyo":
          enemy['hp'] = 20000
        elif enemy['type'] == "boss":
          enemy['hp'] = 10000
      elif enemy['hp'] > 0:
        pass