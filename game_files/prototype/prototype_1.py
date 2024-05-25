From entry import *

class prototype():
    def start():
        print("Welcome to Legacy!")
        a = input("Is your terminal in full screen? y/n").lower()
        b = ["y", "n"]
        while a not in b:
            a = input("Is your terminal in full screen? y/n").lower()
        while a == "n":
            print("Please put your terminal in full screen.")
            a = input("Is your terminal in full screen now? y/n").lower()
        while a == "y":
            pass
            
