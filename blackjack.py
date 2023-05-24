import random
import time

cartas = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
nombre_jugadores = []

def turno_cartas(nombre):
    total = 0
    eleccion = 1
    i = 1
    deck = []
    print("-Turno de", nombre + ":")

    while eleccion != 0 and total < 21:
        numero = random.choice(cartas)
        print("\nCarta #", i, ": ", numero)
        time.sleep(2)

        if numero == "A":
            deck.append(numero)
            print("¿Qué valor quieres que tenga tu 'A', 1 u 11?")
            numero = int(input())
            if numero != 1 and numero != 11:
                print("¡PERDISTE POR TRAMPOSO!")
                return 0
                break
        elif numero in ["J", "Q", "K"]:
            deck.append(numero)
            numero = 10
        else:
            deck.append(numero)

        total += numero
        time.sleep(2)
        if i > 1:
            print("-Total:", total - deck.count("A"))

        if total < 21:
            respuesta = int(input("1) Pedir otra Carta  2) Mirar tus Cartas  3) Finalizar turno\n"))
           # respuesta = int(input("1) Pedir otra Carta   3) Finalizar turno\n"))
            if respuesta == 1:
                i += 1
            elif respuesta == 2:
                print("-Cartas:", deck)
                time.sleep(3) 
        else:
                eleccion = 0
                return total
    else:
            if total == 21:
                print("¡FELICIDADES, has hecho un BLACKJACK!")
            else:
                print("¡QUE MALA SUERTE! HAS PERDIDO!")
            deck.pop() # Elimina la última carta agregada a la lista
            return 0

def obtener_nombres_jugadores(num_jugadores):
    for i in range(num_jugadores):
        print("Introduce el Nombre del Jugador", i + 1)
        nombre = input()
        nombre_jugadores.append(nombre)
    print("-" * 72)

def obtener_ganador_2j(jugador1, jugador2, nombres):
    print("El Ganador es:")
    time.sleep(3)
    if jugador1 > jugador2:
        print(nombres[0], "Con un Total de", jugador1)
    elif jugador2 > jugador1:
        print(nombres[1], "Con un Total de", jugador2)
    elif jugador1 == jugador2:
        print("\n¡Hay un EMPATE! con un Total de", jugador1, "en Ambos Jugadores!")
    else:
        print("\n¡Los 2 Jugadores PERDIERON!")

def obtener_ganador_3j(jugador1, jugador2, jugador3, nombres):
    print("El Ganador es:")
    time.sleep(3)

    if jugador1 > jugador2 and jugador1 > jugador3:
        print(nombres[0], "Con un Total de", jugador1)
    elif jugador2 > jugador1 and jugador2 > jugador3:
        print(nombres[1], "Con un Total de", jugador2)
    elif jugador3 > jugador1 and jugador3 > jugador2:
        print(nombres[2], "Con un Total de", jugador3)
    elif jugador1 == jugador2 and jugador1 != jugador3 and jugador2 != jugador3:
        print("\n¡Hay un EMPATE! entre", nombres[0], "y", nombres[1], "con un Total de", jugador1, "en los Jugadores!")
    elif jugador2 == jugador3 and jugador2 != jugador1 and jugador3 != jugador1:
        print("\n¡Hay un EMPATE! entre", nombres[1], "y", nombres[2], "con un Total de", jugador2, "en los Jugadores!")
    elif jugador1 == jugador3 and jugador1 != jugador2 and jugador3 != jugador2:
        print("\n¡Hay un EMPATE! entre", nombres[0], "y", nombres[2], "con un Total de", jugador1, "en los Jugadores!")
    elif jugador1 == jugador2 and jugador2 == jugador3:
        print("\n¡Hay un EMPATE! con un Total de", jugador1, "en TODOS los Jugadores!")
    else:
        print("\n¡Los 3 Jugadores PERDIERON!")

# MAIN
continuar = 1
while continuar != 0:
    print("JUEGO DE BLACK JACK")
    print("-" * 72)
    num_jugadores = int(input("Número de Jugadores: 1) 1 Jugador  2) 2 Jugadores  3) 3 Jugadores\n"))
    obtener_nombres_jugadores(num_jugadores)

    if num_jugadores == 1:
        print("Buenas, Jugadores. Vamos a empezar la Partida de BlackJack")
        time.sleep(4)
        print("Inicia el Jugador numero 1")
        time.sleep(2)
        jugador1 = turno_cartas(nombre_jugadores[0])
        print("Total del Jugador =", jugador1)
        time.sleep(3)
        continuar = int(input("\n¿Quieres Jugar Otra Vez?  1) Si   0) No\n"))
        del nombre_jugadores[:]
        print("-" * 72)

    elif num_jugadores == 2:
        print("Buenas, Jugadores. Vamos a empezar la Partida de BlackJack")
        time.sleep(4)
        jugador1 = 0
        jugador2 = 0
        for i in range(num_jugadores):
            print("Inicia el Jugador numero", i + 1)
            time.sleep(2)
            if i == 0:
                jugador1 = turno_cartas(nombre_jugadores[i])
                print("Turno Finalizado. Espera a tu Oponente...\n")
                time.sleep(3)
                print("-" * 72)
            else:
                jugador2 = turno_cartas(nombre_jugadores[i])
                print("Turno Finalizado.\n")

        time.sleep(2)
        print("Eligiendo Ganador", end=" ")
        time.sleep(2)
        print(".", end=" ")
        time.sleep(2)
        print(".", end=" ")
        time.sleep(2)
        print(".\n")
        time.sleep(2)

        obtener_ganador_2j(jugador1, jugador2, nombre_jugadores)
        continuar = int(input("\n¿Quieres Jugar Otra Vez?  1) Si   0) No\n"))
        del nombre_jugadores[:]
        print("-" * 72)

    elif num_jugadores == 3:
        print("Buenas, Jugadores. Vamos a empezar la Partida de BlackJack")
        time.sleep(4)
        jugador1 = 0
        jugador2 = 0
        jugador3 = 0
        for i in range(num_jugadores):
            print("Inicia el Jugador numero", i + 1)
            time.sleep(2)
            if i == 0:
                jugador1 = turno_cartas(nombre_jugadores[i])
                print("Turno Finalizado. Espera a tu Oponente...\n")
                time.sleep(3)
                print("-" * 72)
            elif i == 1:
                jugador2 = turno_cartas(nombre_jugadores[i])
                print("Turno Finalizado. Espera a tu Oponente...\n")
                time.sleep(3)
                print("-" * 72)
            else:
                jugador3 = turno_cartas(nombre_jugadores[i])
                print("Turno Finalizado.\n")

        time.sleep(2)
        print("Eligiendo Ganador", end=" ")
        time.sleep(2)
        print(".", end=" ")
        time.sleep(2)
        print(".", end=" ")
        time.sleep(2)
        print(".\n")
        time.sleep(2)

        obtener_ganador_3j(jugador1, jugador2, jugador3, nombre_jugadores)
        continuar = int(input("\n¿Quieres Jugar Otra Vez?  1) Si   0) No\n"))
        del nombre_jugadores[:]
        print("-" * 72)