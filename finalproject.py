import sys
import time
#This creates the sword and torch as variables seen later on in the game.
sword = False
torch = False
#This creates a varaible for the magical scroll and diamond sword in the game
magical_scroll = False
diamond_sword = False
#Class for the protagonist for the story, which contains health points and gold currency
class Protagonist(object):

    def __init__(self, name, health,):
        self.name= name
        self.health = health
        self.gold= 0
class finalboss(object):

    def __init__(self, health,):
        self.health = 150

#Title Screen
print(f'Dungeon Quest ver. 2.36 \n Type any key to start: ')
start = input()
player = Protagonist(input('Enter name here: '), 100)
print(player.name)
#Describes the game for player
print(f'Welcome {player.name}; this game takes place in a mytholigical dungeon during the medival times. \n The dungeon contains numerous monsters and traps, so your survival will rely on the choices you make. ')
#While loop that creates the option to enter the dungeon or to not.
#If the second option is chosen the player will automatically win.
#Else statment just incase player chooses differnt option than chosen.
while True:
    Enter_choice =input("You arrive at the entrance of a menacing dungeon. You have a choice to either enter or go back to your mother. ").lower()
    if Enter_choice in ["enter", "enter the dungeon",]:
        print("You make the idiotic choice of entering a dangerous dungeon with no supplies. Good Luck")
        break
    elif Enter_choice=="go back to my mother":
        print("Smart Choice. Game Over. You Win")
        time.sleep(10)
        sys.exit()
    else:
        print("That was not an option given, choose either Enter or go back home to my mother")
#While loop that creates the option to fight or run
#The protagonist class is used to to show damage given by enemies.
while True:
    Fight_choice=input("After exploring the dungeon for while. You run into a skeleton monster. Fight it or Run away. ").lower()
    if Fight_choice in ['fight it', 'fight', 'fight skeleton', 'fight skeleton monster']:
        player.health = player.health - 20
        print('You somehow beat the skeleton monster and gained a sword and torch from it. You however suffer some damage.')
        print(f'Your health has decreased by 20 points.  It is now {player.health} points.')
        sword = True
        torch = True
        if sword == True and torch == True:
            break
    elif Fight_choice in ['run', 'run away']:
        print("You successfully escape, but miss out on the oppurtunity to loot the skelton of its sword and torch. \n Now you are more vunerable to stronger monsters.")
        break

    else:
        print("That was not an option given, choose either fight or run away")
#While loop that creates the option to enter or ignore the room
#If you obtained the sword and torch from the last choice. You will be able to enter the room without taking damage. And obtain direction on which path to take.
#If you did not obtain the torch and sword and enter you will die.
#If you chose to ignore the room you would you would have to guess on the next option
while True:
    Room_choice=input("You explore deeper into the the dungeon and you find a dark room. Enter the room or ingore the room? ")
    if Room_choice in ["enter","enter room", "enter the room"]:
        print("You enter the room and since you have a sword and torch you catch the monsters off guard and kill them without taking damage. \n These monsters drop a map to the treasure of dungeon. The treasure map shows that the main treasure of the dungeon is on the right")
        break

    elif torch != True and sword != True:
        player.health = player.health - 80
        print("You enter the dark and mysterious room without any weapon or torch. The goblins in the room use the darkness to ambush you. \n You suffer a devasting amount of damage.")
        print(f'Your health has decreased by 80 points.  It is now {player.health} points.')
        print("Game Over. You Lose.")
        time.sleep(10)
        sys.exit()


    elif Room_choice in ["ignore", "ignore the room", "ignore room"]:
        print("You choose to ignore the room... wuss.")

    else:
         print("That was not an option given, choose either Enter or ignore")
#While loop that creates the option to go right or left.
#Going right will continue the game and left will result in death
while True:
    Path_choice=input(" You find yourself in the middle of two paths of the dungeon do you go right or left? ")
    if Path_choice in ["go right","right", "go to the right"]:
        print("The path to the right leads you to a mound of treasure but is guarded by the dungeon's mini boss,a giant cyclops. \n The entrance to the room shuts behind you, so the only way to survive is to kill the cylops.")
        break

    elif Path_choice in ["go left","left", "go to the left"]:
        print("Turns out that was a trap which you fall into and get impaled by multiple spikes.\n Game Over")
        time.sleep(10)
        sys.exit()

    else:
        print("That was not an option given choose either left or right")
#While loop that creates the option to fight or wait.
#Fighting will result in death and waiting will continue the story and give the player gold coins
while True:
    FightClarence_choice=input("Attack the cyclops first or wait for the cyclops to make a move ")
    if FightClarence_choice in ["attack","attack cyclops", "attack the cyclops"]:
        print("You chose to fight a giant cyclops head on... ok. Well to keep it short the cyclops crushes your skull and you die. \n Game Over")
        time.sleep(10)
        sys.exit()
        break

    elif FightClarence_choice in ["wait", "wait for the cyclops to make a move", "wait for cyclops"]:
        print("To your suprise the cyclops actually a pretty chill dude named Clarence.\n Clarence lets you take some of the treasure and lets you go deeper into the dungeon.")
        player.gold = +50
        print(f'You have recived {player.gold} gold coins!.')
        break

    else:
         print("That was not an option given choose either fight or wait")
#While loop that creates the option to choose the item of choice
#Buying sword will eventually result in death because it is cursed
#Buying scroll may result in victory
while True:
    Shop_choice=input("Beyond the lair of the cyclops is a shop ran by a ghost. The shop is selling magic scroll and a diamond sword for 50 coins. \n Buy the sword or scroll " )
    if Shop_choice in ["magic scroll", "buy scroll", "buy magic scroll", "scroll"]:
        player.gold = player.gold -50
        print(f'You now have {player.gold} gold coins.')
        print("You purchased the mystical scroll with no idea of it's abilities, but it looks useful.")
        magical_scroll = True
        break
    elif Shop_choice in ["diamond sword","buy diamond sword", "sword"]:
        player.gold =player.gold -50
        print(f'You now have {player.gold} gold coins.')
        print("You purchased the dangerous looking sword")
        diamond_sword=True
        break
    else:
         print("That was not an option given choose either sword or scroll")

#Player not given choice. Story continues automatically
Finalroom_choice=input("Now that you have bought your item of choice you are now ready to fight the dungeon boss. Are you ready? Yes or no")
print("It really doesnt matter if you're ready. You have no choice")

#While loop that creates the options based on the weapon chosen
#Players will die either way if they have the sword
#Players can only win if they pick fireball spell.
while True:
    if diamond_sword == True:
        print("You are face to face with the boss of the dungeon, an orge who kind of resembles shrek")
        attack_choice= input("Attack with your sword or defend?" )
        if attack_choice in ["attack", "attack with sword", "attack orge", "defend", "defend with sword"]:
            print("You died... I forgot to mention that sword was cursed. \n Game Over.")
            break
    elif magical_scroll== True:
        print("You are face to face with the boss of the dungeon, an orge who kind of resembles shrek.")
        spell_choice= input("The magical scroll is now glowing and gives you the option to use a fire ball spell or lightining spell. ")
        if spell_choice in ["lightining", "lightining spell"]:
            print("The lighting spell worked and struck the area you casted it in, causing you to die by lightining strike. \n Game Over.")
            break
        elif spell_choice in ["fire spell", "fire ball spell", "fire ball", "fire"]:
            print('The fire ball spell incinerated the giant orgre. You survied the dungeon and beat the game... congrats I guess. \n You Win!')
            break