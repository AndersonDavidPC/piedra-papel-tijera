import random
optionList = ["piedra", "papel", "tijera"]

def iniciarJuego():
    print("Juego iniciado")

def opcionUser():
    # Aquí va el código para obtener la elección del jugador
    opcionUser = input("Elije piedra, papel o tijera: ")
    #Validación de la opción del usuario
    while opcionUser not in optionList:
        opcionUser = input("Elije piedra, papel o tijera: ")
    return opcionUser

def opcionPC():
    # Aquí va el código para obtener la elección de la computadora
    opcionPC = random.choice(optionList)
    print("La computadora eligió: ", opcionPC)
    return opcionPC

def ganador(opcionUser, opcionPC):
    # Aquí va el código para determinar el ganador
    if opcionUser == opcionPC:
        return "Empate"
    elif opcionUser == "piedra" and opcionPC == "tijera":
        return "Ganaste"
    elif opcionUser == "papel" and opcionPC == "piedra":
        return "Ganaste"
    elif opcionUser == "tijera" and opcionPC == "papel":
        return "Ganaste"
    else:
        return "Perdiste"
    
def score(ptsUser, ptsPC):
    print("Marcador: ", ptsUser, " - ", ptsPC)

#Juego al mejor de 3
def main():
    iniciarJuego()
    rounds = 0
    ptsUser = 0
    ptsPC = 0
    while rounds < 3:
        rounds += 1
        print("Ronda: ", rounds)
        opUser=opcionUser()
        opPC=opcionPC()
        ganador(opUser, opPC)
        if ganador(opUser, opPC) == "Ganaste":
            ptsUser += 1
        elif ganador(opUser, opPC) == "Perdiste":
            ptsPC += 1
        else:
            rounds -= 1
        score(ptsUser, ptsPC)
    #Determinar el ganador del juego
    if ptsUser > ptsPC:
        print("Ganaste el juego")
    else:
        print("Perdiste el juego")
    print("Fin del juego")

main()