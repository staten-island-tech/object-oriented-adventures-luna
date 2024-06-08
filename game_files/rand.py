import os


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