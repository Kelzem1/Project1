name = input("Hey type your name: ")
nameUpper = name.upper()
print("Hello "+ nameUpper + " welcome to my game!")

should_we_play = input("Do you want to play? ").lower()

#Hacer lo siguiente cuando avances mas en el curso de python. Necesario recordar objetos en python
#Crear una funcion para elegir el personaje. 3 opciones(Guerrero, Ada, Mago)
#Crear una funcion para el combate contra el monstruo. Mediante un lanzamiento de dados


def monster():
    
    monster = input("You find the Monster. You want to fight or run? (Type fight/run) ").lower()
    if monster == "fight":
            print("You kill the Monster! YOU WIN!!!")
    else:
            print("The Monster follows you and he eat you! YOU DIE!!")


def firstDirection():
    direction = input("You wanna go left or right? (Type left/right)").lower()
    if direction == "right":
        monster()
    else:
        print("You go left and finds Pedro Sanchez. END GAME!")
            


if should_we_play == "yes" or should_we_play == "y":
    print("We are gonna play!!")
    firstDirection()
else:
    print("OK, see you later!")