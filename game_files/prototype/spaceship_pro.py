import sys
sys.path.append("game_files")
from rand import *
from spaceship import *

class pro():
  def wel(username):
     spaceship.welcome(username)
     answer = input("")
     a = ["1", "2", "3"]
     while answer not in a:
       print("Xingxing: Choose again! You can't just make your own choices!!")
       answer = input("")
     print("Xingxing: Hmm. Alright then. Let's go.")
     rand.load()
     if answer == "1":
       print("Xingxing: What type of mission are you going on this time?")
       rand.quest_selector(username)
       b = ["S", "D"]
       quest = input("").upper()
       while quest not in b:
         print("Xingxing: What did I say! What do you want to do anyways!?")
         quest = input("").upper()
       print("Xingxing: Hmm...I see.")
       if quest == "S":
         spaceship.quest_story(username)
       elif quest == "D":
         spaceship.daily(username)
       rand.contin()
     elif answer == "2":
       spaceship.star_system(username)
     elif answer == "3":
       spaceship.select_character(username)
     pro.wel(username)
