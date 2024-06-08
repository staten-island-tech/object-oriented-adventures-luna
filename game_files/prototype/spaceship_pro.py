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
       spaceship.quest_story(username)
     elif answer == "2":
       spaceship.star_system(username)
     elif answer == "3":
       spaceship.team(username)
     pro.wel(username)
