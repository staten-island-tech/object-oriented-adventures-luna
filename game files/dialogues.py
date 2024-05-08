import os
""" os.system("cls") """        # how to clear the terminal

class dialogues_story():
    def prologue(x):            # x can't be greater than 3 (lowest number = 0)
        dialogue = ["You and your sibling are travelers across worlds. Frome time to time, you stop by the space station for supplies. But this time, something big happened....", 
                    "The Oblivion, a cult who follows the path of destruction, has invaded the space station.", 
                    "You try and stop them in their tracks before they take all the supplies from the space station, but you fail...", 
                    "You feel your consciousness fade into the void as your kin was abducted, unaware of all that just occurred."]
        print(dialogue[x])
    def space_station(x):       # x can't be greater than 16
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
        print(dialogue[x])
    def getting_asahi(x):
        dialogue = ["You got Asahi!!!!!"]
    def monde(x):              # x can't be greater than 18
        dialogue = ["Asahi: Are you ready to go?", 
                    "It has already been a few days since you decided to join the Legacy.", 
                    "Asahi: Here is the world, Monde. They worship the god of Erudition. The world has seen better days, but now...", 
                    "Asahi: Mainly water remains. Humanity has all scattered on this planet.", 
                    "Asahi: Look! We're landing now!", 
                    "As he says that, the spaceship begins to land.", 
                    "Looking around you see a world of blue. It seems as if the water had engulfed all the land in this world.", 
                    "As you get closer to the surface, you see archipelagos filled with small settlements, all scattered.", 
                    "Asahi: Look, there you might be able to find your sibling.", 
                    "Asahi: Be careful though. There are many dangers that lurk on these islands.", #battle
                    "Asahi: They might not look it, but they are more advanced in technology than other civilizations that you ever encounter.", 
                    "Asahi: What?", 
                    "Asahi: Really.", 
                    "Asahi: Alright then. Let's go now.", 
                    "Asahi: Look up there.", 
                    "Looking up, you see a message in the sky.", 
                    "Asahi: I see then let's go there next then.", 
                    "Asahi: Pero.",
                    "Soon, the adventure in Monde has come to an end. A clue from your sibling has been found."]
        print(dialogue[x])
    def pero(x):                # x can't be greater than 26
        dialogue = ["Looking around the spaceship, you wonder about what has just occured on Monde.", 
                    "You found a clue on your sibling's location.", 
                    "Asahi: You seem quite determined.", 
                    "Asahi: I see.", 
                    "Asahi: Well, I can't quite go to this world with you just yet.", 
                    "Asahi: The spaceship is in need of fixing.", 
                    "Asahi: Someone else will be joining you for this adventure.", 
                    "Asahi: She's just a bit more convervative...", 
                    "Looking around you see a purple haired woman walking towards you, her long hair glistening in the starlight.", 
                    "Asahi: Say hi to your partner for the mission!", 
                    "Asahi: Mael!",
                    "Mael: Hi.",
                    "Based off of her short yet simple style of talking, you could tell that",
                    "this is going to be a long trip."
                    "Soon,the two of you set off on your journey to the new world, Pero.", 
                    "You had learned from Asahi that this is the world that follows the path of Harmony,", 
                    "but right now the planet is in dissarray due to the recent raids from the Oblivion.", 
                    "It seems that after the defeat on the Space Ship, they have went to other planets.", 
                    "Mael: We're landing.", 
                    "Mael: ...",
                    "Mael: Watchout!",
                    "Mael: ...",
                    "You find a scroll on the floor.", 
                    "You then see a message on the paper, in a writing that you aren't familiar with.", 
                    "Mael: Asahi will probably be able to read it.", 
                    "Looking over your shoulder, you see Mael looking at the scroll intently.", 
                    "With that this journey concludes and you and Mael go back to the ship with the scroll."]
        print(dialogue[x])
    def taiyo(x):
        dialogue = ["Back at the space ship, you and Mael rush towards Asahi's room to deciper the message.", 
                    "Asahi: Oh, hi.", 
                    "Mael: ...", 
                    "Asahi: How was your adventure in Pero?", 
                    "Asahi: I see.", 
                    "Asahi: Sure.", 
                    "As Asahi translates the scroll for you, his face begins to darken.", 
                    "Asahi: It seems that your next destination in Taiyo.", 
                    "Asahi: I'm afraid you would need to go to Taiyo with Mael.", 
                    "Mael: Alright.", 
                    "Asahi: It's complicated.", 
                    "Asahi: Sure.", 
                    "Mael: Should we head out now?", 
                    "Asahi: Bye.", 
                    "As you leave for Taiyo, you hope that your sibling is there.", 
                    "Mael: We've arrived.", 
                    "Mael: The planet of Nihility.", 
                    "Moving around, you see that the planet is more developed than the other planets you have encountered.", 
                    "You see shrines, townhouses, walls, statues, and other larege monuments in the distance.", 
                    "Soon, you arrive at the center of the town, and you are stopped by the guards.", 
                    "Mael: Are you alright?", 
                    "Unknown: Are you guys alright?", 
                    "Looking up, you see Asahi in a spaceship.", 
                    "Together you guys defeat the queen of the planet. And a stone falls on the ground.", 
                    "It's redish hue, similar to that of blood, shines in the sun.", 
                    "You contemplate whether or not to pick it up or not...", 
                    "You choose to pick up the stone, and as you go to pick it up, the stone glows. You see your sibling standing in front of you. (Happy Ending)", 
                    "You choose to leave the stone alone, and go back to the spaceship empty handed. Still, looking around yoiu see your new friends and find peace in that.", 
                    "You hope that one day you will be able to fiund your sibling, but for now you are content with your current situation. (Legacy Ending)"]
        print(dialogue[x])

class dialogues_quest():
    def monde(x):
        dialogue = ["Do you wish to begin your adventure to Monde?"]
        print(dialogue[x])
    def pero(x):
        dialogue = ["Do you wish to head to Pero?"]
        print(dialogue[x])
    def taiyo(x):
        dialogue = ["Do you wish to head to the final world, Taiyo? The journey may be harsh."]
        print(dialogue[x])
    def transition(x):
        dialogue = 

    
class dialogues_player():
    def space_station(x):
        dialogue = ["You: I think I'm fine. Who are you?",
                    "You: Did you see anyone else?",
                    "You: I think I've been separated from my sibling.",
                    "You: Then...",
                    "You: Okay, thanks for watching out for me.",
                    "You: Yeah, but they seem dangerous.", #X8
                    "You: Erm.. what're those...", #X8
                    "You: We shouldn't just stand here.", #X9
                    "You: Oh god", #X9
                    "You: Phew.. I carried", #x10    
                    "You: Aw man..", #x11
                    "You: It's alright. Where there's a will, there's a way.", #x11
                    "You: Travel with the Legacy? Of course!", #choices for which path player will take
                    "You: I'd rather search for my sibling on my own."]
        print(dialogue[x])
    def monde(x):
        dialogue = ["You: [a] Nuh uh. [b] Duh.", #x0
                    "You: [a] Yikes.. what on earth happened here? [b] It's still gorgeous in my eyes.", #x2
                    "You: What a shame.",
                    "You: Woohoo!",
                    "You: Here we go...",
                    "You: Yeah. I hope I find them soon.",
                    "You: [a] More bad guys?? I'm tired of fighting! [b] Aaaaaaaaaaaaaaaaaaaaaa [c] Light work", #x9
                    "You: Well... those robots seemed...",
                    "You: [a] ..pretty old. They were all rusty and it didn't take much for them to break. [b] ..pretty strong. I almost lost an arm.", #x11
                    "You: Yup. I think we've checked everything out here."
                    "You: What is that?",
                    "You: Make your way to the land of ice, where the trolls reside?",
                    "You: Where is that?"]
        print(dialogue[x])
    def pero(x):
        dialogue = ["You: Well we've already come this far, and my sibling means a lot to me.",
                    "You: [a] ..Why not? [b] Bailing out already?", #x4
                    "You: Who?", #X6
                    "You: [a] Hi...? [b] HI!!!!!!!!!!!!!!", #X9
                    "You: Oh my god", #x20
                    "You: [a] Looks like they dropped something. [b] Booty?!", #x21
                    "You: [a] What can't he do... he seems smart afterall. [b] Nerd"] #x24
        print(dialogue[x])
    def taiyo(x):
        dialogue = ["You: We're finally back..", #after x0
                    "You: [a] Well. It was something for sure. [b] I GOT THE BOOTY", #x3
                    "You: Could you take a look at this? We found it in Pero.",
                    "You: Is something wrong?",
                    "You: You're staying back again? Are you gonna come later on?",
                    "You: Yeah. Let's go.",
                    "You: Soooo.. which planet is this?"
                    "You: [a] You're finally here. [b] Took you long enough."
                    "Pick up the stone? [a] Yes [b] No"]
        print(dialogue[x])
        
class dialogues_tutorial():
    def spaceship(x):
        dialogue = ["Captain: Tutorial time!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
                    "Captain: You're gonna be beating up a lot of enemies, so you'll need to know the controls. "]
