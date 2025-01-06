

name = input("Hey type your name: ")
nameUpper = name.upper()
print  ("Hello "+ nameUpper + " welcome to my game!")

should_we_play = input("Do you want to play? ").lower()

#Hacer lo siguiente cuando avances mas en el curso de python. Necesario recordar objetos en python
#Crear una funcion para elegir el personaje. 3 opciones(Guerrero, Ada, Mago)
#Crear una funcion para el combate contra el monstruo. Mediante un lanzamiento de dados


def monster():
    
    monster = input("You find the Monster. You want to fight or run? (Type fight/run) ").lower()
    if monster == "fight":
            print("You fight the monster and obviusly you die... Stupid...\n")
            print("")
    else:
            print("The Monster follows you and he eat you! YOU DIE!!")
            
def fishing():
    fishing = input("You find a river. You can fishing in the river. You wanto to?").lower()
    print("")
    if fishing == "yes":
        print("I LOVE YOU!!. YOU GET A BIT FISH AND WIN THE GAME. YOU ARE LIKE ME!!")
    else:
        print("You cross the river and a water monster kills you!... Stupid...")


def firstDirection():
    direction = input("You wanna go left or right? (Type left/right)").lower()
    if direction == "right":
        monster()
    else:
        fishing()
            


if should_we_play == "yes" or should_we_play == "y":
    print("We are gonna play!!")
    firstDirection()
else:
    print("OK, see you later!")