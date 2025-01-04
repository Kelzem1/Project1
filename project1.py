name = input("Hey type your name: ")
nameUpper = name.upper()
print("Hello "+ nameUpper + " welcome to my game!")

should_we_play = input("Do you want to play? ").lower()

def firstDirection():
    direction = input("You wanna go left or right? ").lower()
    if direction == "right":
        monster = input("You find the Monster. You want to fight or run? ").lower()
        if monster == "fight":
            print("You kill the Monster! YOU WIN!!!")
        else:
            print("The Monster follows you and he eat you! YOU DIE!!")
    else:
        print("You go left and finds Pedro Sanchez. END GAME!")
            


if should_we_play == "yes" or should_we_play == "y":
    print("We are gonna play!!")
    firstDirection()
else:
    print("OK, see you later!")