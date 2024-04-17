import os
""" os.system("cls") """        # how to clear the terminal

class dialogues_npc():
    def prologue(x):            # x can't be greater than 3 (lowest number = 0)
        dialogue = ["You and your sibling are travelers across worlds. Frome time to time, you stop by the space station for supplies. But this time, something big happened....", 
                    "The Oblivion, a cult who follows the path of destruction, has invaded the space station.", 
                    "You try and stop them in their tracks before they take all the supplies from the space station, but you fail...", 
                    "You feel your consciousness fade into the void as your kin was abducted, unaware of all that just occurred."]
        print(dialogue[x])
    def space_station(x):
        dialogue = ["Waking up, you see a young man who seems to in his late teens next to you.", 
                    "Looking around, you see that you are in the space station infirmary, your sibling no where to be seen.", 
                    "Asahi: Hey there. Are you okay? You were unconcious for a while there, thankfully we found you before anything else happened.", 
                    "Asahi: Oh, I am Asahi, a traveller from the group, Legacy. We came to the space station to refill on supplies when we found you here.", 
                    "Asahi: No, you were alone when we found you.", 
                    "Asahi: I see, well the space station is still filled with guards from the Oblivion. It's not safe to travel alone right now....", 
                    "Asahi: How about you rest up first and recover before we head out to look for your sibling?", 
                    "One week later, you and your new companion are walking around the space station looking for your sibling when you ran into the Oblivion guards.", 
                    "Asahi: Are you alright?", 
                    "Asahi: Look out, there's more of them.", 
                    "Asahi: Finally, it's over.", 
                    "Asahi: It doesn't seem like your sibling is here.", 
                    "Asahi: Would you like to travel with us?", 
                    "Asahi: Great!",                                    # The last four lines, two of them might not be used based off of the player's choice
                    "Asahi: Oh then be careful."
                    "As you depart from the space station alone in search of your sibling, you travel to many worlds after world with not even finding a sliver of your sibling's hair. This journey would continue until the end of your life.", 
                    "As you depart from the space station with 'The Legacy', you ponder over what the future might hold for you."]
    def monde(x):
        pass