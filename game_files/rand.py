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
  def attk_full(x, y, z, t):
    used = x
    enemy_team = y
    attack = z
    for enemy in enemy_team:
      if enemy not in used:
        e = enemy['hp']
        if t == 'u':
          enemy['hp'] = e - (attack/3)
        elif t == 'a':
          enemy['hp'] = e - (attack/2)
      elif enemy in used:
        pass
  def hp_full(x):
    enemy_team = x
    for enemy in enemy_team:
            if enemy['hp'] <= 0:
              if enemy['name'] == "Oblivion Guard":
                enemy['hp'] = 4500
              elif enemy['name'] == "Oblivion Drone":
                enemy['hp'] = 4500
              elif enemy['name'] == "General Aeron":
               enemy['hp'] = 10000
              elif enemy['name'] == "Hydro Robot":
               enemy['hp'] = 4500
              elif enemy['name'] == "Hydro Robot Dog":
               enemy['hp'] = 4500
              elif enemy['name'] == "Giant Hydro Robot":
               enemy['hp'] = 10000
              elif enemy['name'] == "Ice Goblin":
               enemy['hp'] = 4500
              elif enemy['name'] == "Ice Archer Goblin":
               enemy['hp'] = 4500
              elif enemy['name'] == "Oblivion Orb":
               enemy['hp'] = 4500
              elif enemy['name'] == "Yeti":
               enemy['hp'] = 10000
              elif enemy['name'] == "Trainee Guard":
               enemy['hp'] = 4500
              elif enemy['name'] == "Guard":
               enemy['hp'] = 4500
              elif enemy['name'] == "Guard Captain":
               enemy['hp'] = 10000
              elif enemy['name'] == "Queen of Taiyo":
               enemy['hp'] = 20000
            else:
              pass