import os
import json

with open (r"game_files\classes\json\users.json", "r") as hi : 
  users = json.load(hi)


class random():
  def contin():
    c = input("[A] Continue").upper()
    while c != "A":
      c = input("").upper()
    os.system("cls")
  def load():
    for i in range(20):
      print("loading '")
      os.system("cls")
      print("loading !")
      os.system("cls")
      print("loading ,")
      os.system("cls")
      print("loading .")
      os.system("cls")
      print("loading ;")
      os.system("cls")
      print("loading *")
      os.system("cls")
  def quest_selector(username):
    for user in users:
      if user['username'] == username:
        data = len(user['quest'])
    print("[S] Story Quest")
    if data > 1:
      print("[D] Dailies")