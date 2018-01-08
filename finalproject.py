name = input('enter name here: ')
print(f'Welcome {name}; this game will place you in a virtual dungeon. Your survival will depend on your decisions ')
while True:
    torch_choice=input("You walk into th dungeon do you want to pick up a sword or torch? ").lower()
    if torch_choice== "torch":
        print("You use the torch to clearly see the pathways in the dungeon")
        break
    elif torch_choice=="sword":
        print("bla")
        break
    else:
        print("That was not an option given, choose either torch or sword")
