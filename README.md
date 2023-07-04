# Juego de Piedra, Papel y Tijera

Este es un programa simple en Python que implementa el juego de Piedra, Papel y Tijera. El juego permite al usuario jugar contra la computadora al mejor de tres rondas.

## Instrucciones

1. Ejecuta el programa en Python para iniciar el juego.
2. En cada ronda, se te pedirá que elijas entre "piedra", "papel" o "tijera".
3. Escribe tu elección en la consola y presiona Enter.
4. La computadora elegirá al azar una de las opciones.
5. El programa determinará el ganador de la ronda y mostrará el marcador actualizado.
6. El juego continuará hasta que se hayan jugado tres rondas.
7. Al finalizar, se anunciará el ganador del juego.

## Código

```python
import random

optionList = ["piedra", "papel", "tijera"]

def iniciarJuego():
    print("Juego iniciado")

def opcionUser():
    # Aquí va el código para obtener la elección del jugador
    opcionUser = input("Elije piedra, papel o tijera: ")
    # Validación de la opción del usuario
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

# Juego al mejor de 3
def main():
    iniciarJuego()
    rounds = 0
    ptsUser = 0
    ptsPC = 0
    while rounds < 3:
        rounds += 1
        print("Ronda: ", rounds)
        opUser = opcionUser()
        opPC = opcionPC()
        ganador(opUser, opPC)
        if ganador(opUser, opPC) == "Ganaste":
            ptsUser += 1
        elif ganador(opUser, opPC) == "Perdiste":
            ptsPC += 1
        else:
            rounds -= 1
        score(ptsUser, ptsPC)
    
    # Determinar el ganador del juego
    if ptsUser > ptsPC:
        print("Ganaste el juego")
    else:
        print("Perdiste el juego")
    
    print("Fin del juego")

main()
```

¡Diviértete jugando al Piedra, Papel y Tijera!