class prologue():
    def start(username):
        print("Pick your character: ")
        print("[A] Aelius")
        print("[B] Amaris")
        print("Please note that you will not be able to change your character once you have chosen the one you want.")
        a = input("").lower()
        b = ["a", "b"]
        while a not in b:
            print("Please choose again! That was not one of the options.")
            a = input("").lower()
        if a == b[0]:
            