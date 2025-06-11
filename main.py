from cave import Cave
from character import Enemy
from character import Enemy, Friend
from item import Item


# create cave objects
cavern = Cave("Cavern")
cavern.set_description("A dank and dirty cave\n")

dungeon = Cave("Dungeon")
dungeon.set_description("A large cave with a rack\n")

grotto = Cave("Grotto")
grotto.set_description("A small cave with ancient graffiti\n")

dungeon.link_cave(grotto, "west")
dungeon.link_cave(cavern, "north")
cavern.link_cave(dungeon, "south")
grotto.link_cave(dungeon, "east")

# create character objects
lucas = Enemy("Lucas Yang", "A smelly Fortnite player")
lucas.set_conversation("200")
lucas.set_weakness("studying")
dungeon.set_character(lucas)

josephine = Friend("Josephine", "A friendly bat")
josephine.set_conversation("Gidday")
grotto.set_character(josephine)

cheese = Item("Cheese", "A smelly piece of cheese")

cavern.set_item(cheese)

current_cave = cavern
dead = False
while dead == False:      	
    print("\n")         
    current_cave.get_details()
    inhabitant = current_cave.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ")    
   
    if command in ["north", "south", "east", "west"]:
            current_cave = current_cave.move(command)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                # What happens if you win?
                print("Bravo, hero you won the fight!")
                current_cave.set_character(None)
            else:
                print("Scurry home, you lost the fight.")
        else:
            print("There is no one here to fight with")
    elif command == "pat":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you…")
            else:
                inhabitant.pat()
        else:
            print("There is no one here to pat :(")
    elif command == "quit":
        print("Thanks for playing!")
        dead = True
    
