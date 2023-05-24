import random
APUESTA_MINIMA_CASINO = 2000
APUESTA_MINIMA_RULETA = 10000
CANTIDAD_FIJA_CASINO = 2000  # La cantidad fija que se pierde o gana
# Cantidad que se gana cuando se acierta entre par e impar
DINERO_GANADO_PARIDAD = 15000
menu_juegos = """1. Casino
2. Ruleta
3. Salir
Elige: """
sintesis_casino = f"""Casino: apuesta y gira la ruleta de las siguientes opciones:
Multiplicar la apuesta x 2
Restar 50 % a la apuesta
Ganar una cantidad fija {CANTIDAD_FIJA_CASINO}
Perder una cantidad fija {CANTIDAD_FIJA_CASINO}
Perder toda la apuesta"""
sintesis_ruleta = f"""Ruleta: se puede apostar por:
Número y color. Si aciertas ambos, la apuesta se multiplica por 10. Si no, se pierde la apuesta
Solo color: si se acierta el color, la apuesta se multiplica por 2. Si no, pierde la apuesta
Solo paridad: si se acierta entre las opciones de número par o impar, se ganan {DINERO_GANADO_PARIDAD} pesos. Si no, se pierde la apuesta
Los colores van del 1 al 20, colores son rojo y negro; paridades son par e impar"""
# Constantes para las opciones del casino
MULTIPLICAR_APUESTA = 1
RESTAR_PORCENTAJE_APUESTA = 2
GANAR_CANTIDAD_FIJA = 3
PERDER_CANTIDAD_FIJA = 4
PERDER_TODO = 5
COLOR_NEGRO = "Negro"
COLOR_ROJO = "Rojo"
IMPAR = "Impar"
PAR = "Par"


def solicitar_dinero_apostar_casino(saldo):
    dinero_apostado = 0
    while dinero_apostado < APUESTA_MINIMA_CASINO or dinero_apostado > saldo:
        dinero_apostado = float(
            input(f"¿Cuánto apuestas? debe ser al menos {APUESTA_MINIMA_CASINO} pesos y no debe superar el saldo: "))
    return dinero_apostado


def solicitar_dinero_apostar_ruleta(saldo):
    dinero_apostado = 0
    while dinero_apostado < APUESTA_MINIMA_RULETA or dinero_apostado > saldo:
        dinero_apostado = float(
            input(f"¿Cuánto apuestas? debe ser al menos {APUESTA_MINIMA_RULETA} pesos y no debe superar el saldo: "))
    return dinero_apostado


def solicitar_numeros(cantidad):
    numeros = []
    contador = 0
    while contador < cantidad:
        numero = 0
        while numero < 1 or numero > 20:
            numero = int(input("Elige un número entre 1 y 20: "))
        numeros.append(numero)
        contador += 1
    return numeros


def main():
    # El saldo con el que inicia
    saldo_global = 50000
    eleccion = ""
    while eleccion != "3":
        eleccion = input(menu_juegos)
        if eleccion == "1":
            if saldo_global < APUESTA_MINIMA_CASINO:
                print(
                    f"Necesita contar con un saldo de al menos {APUESTA_MINIMA_CASINO} para jugar al casino")
                continue
            print(sintesis_casino)
            print(f"Dinero disponible: {saldo_global}")
            dinero_apostado = solicitar_dinero_apostar_casino(saldo_global)
            eleccion_casino = ""
            while eleccion_casino != "3":
                print(f"Dinero disponible: {saldo_global}")
                eleccion_casino = input("""1. Girar ruleta
2. Modificar monto apostado
3. Volver
Elige: """)
                if eleccion_casino == "1":
                    if saldo_global < APUESTA_MINIMA_CASINO:
                        print(
                            f"Necesita contar con un saldo de al menos {APUESTA_MINIMA_CASINO} para jugar al casino")
                        break
                    ruleta = [MULTIPLICAR_APUESTA, RESTAR_PORCENTAJE_APUESTA,
                              GANAR_CANTIDAD_FIJA, PERDER_CANTIDAD_FIJA, PERDER_TODO]
                    # Elegimos una opción aleatoria
                    indice_aleatorio = random.randint(0, len(ruleta)-1)
                    opcion = ruleta[indice_aleatorio]
                    if opcion == MULTIPLICAR_APUESTA:
                        print("La apuesta se multiplica por dos")
                        saldo_global += dinero_apostado
                    elif opcion == RESTAR_PORCENTAJE_APUESTA:
                        print("Se resta el 50 %")
                        saldo_global -= dinero_apostado / 2
                    elif opcion == GANAR_CANTIDAD_FIJA:
                        print(f"Se ganan {CANTIDAD_FIJA_CASINO} pesos")
                        saldo_global += CANTIDAD_FIJA_CASINO - dinero_apostado
                    elif opcion == PERDER_CANTIDAD_FIJA:
                        print(f"Se pierden {CANTIDAD_FIJA_CASINO} pesos")
                        saldo_global -= CANTIDAD_FIJA_CASINO
                    else:
                        print("Pierde todo lo apostado")
                        saldo_global -= dinero_apostado
                elif eleccion_casino == "2":
                    dinero_apostado = solicitar_dinero_apostar_casino(
                        saldo_global)
        elif eleccion == "2":
            print(f"Dinero disponible: {saldo_global}")
            colores = [COLOR_ROJO, COLOR_NEGRO]
            if saldo_global < APUESTA_MINIMA_RULETA:
                print(
                    f"Necesitas al menos {APUESTA_MINIMA_RULETA} pesos para jugar a la ruleta")
                continue
            print(sintesis_ruleta)
            dinero_apostado = solicitar_dinero_apostar_ruleta(saldo_global)
            eleccion_ruleta = ""
            while eleccion_ruleta != "4":

                print(f"Dinero disponible: {saldo_global}")
                eleccion_ruleta = input("""1. Número y color
2. Solo color (negro y rojo)
3. Paridad (par e impar)
4. Volver
Elige: """)
                if eleccion_ruleta == "1":
                    if saldo_global < APUESTA_MINIMA_RULETA:
                        print(
                            f"Necesitas al menos {APUESTA_MINIMA_RULETA} pesos para jugar a la ruleta")
                        break
                    valor= int (input("ingrese la cantidad de numeros que quiere apostar en la ruleta "))
                    numero_usuario = []
                    numero_usuario = solicitar_numeros(valor)
                    color_eleccion_usuario = input(
                        "1. Rojo\n2. Negro\nElige: ")
                    if color_eleccion_usuario == "1":
                        color_usuario = COLOR_ROJO
                    else:
                        color_usuario = COLOR_NEGRO
                    # Elegir aleatoriamente
                    numero_aleatorio = random.randint(1, 20)
                    #color_aleatorio = colores[random.randint(0, len(colores)-1)]
                    color_aleatorio = COLOR_NEGRO
                    print("Número obtenido: " + str(numero_aleatorio))
                    print("Color obtenido: " + str(color_aleatorio))
                    a=0
                    dinero_apuesta_final=dinero_apostado/valor
                    for numero in numero_usuario:
                        if numero_aleatorio == numero and color_aleatorio == color_usuario:
                             # El usuario acierta
                                print("Gana el dinero apostado multiplicado por 10", dinero_apuesta_final * 9)
                                saldo_global += dinero_apuesta_final * 9
                                a = 1
                                break
                    if a==0:
                            print("Pierde lo apostado")
                            saldo_global -= dinero_apostado
                    pass
                elif eleccion_ruleta == "2":

                    if saldo_global < APUESTA_MINIMA_RULETA:
                        print(
                            f"Necesitas al menos {APUESTA_MINIMA_RULETA} pesos para jugar a la ruleta")
                        break
                    color_eleccion_usuario = input("1. Rojo\n2. Negro\nElige:")
                    if color_eleccion_usuario == "1":
                        color_usuario = COLOR_ROJO
                    else:
                        color_usuario = COLOR_NEGRO
                    color_aleatorio = colores[random.randint(
                        0, len(colores)-1)]
                    print("Color obtenido: " + color_aleatorio)
                    if color_usuario == color_aleatorio:
                        # Acierta
                        print("La apuesta se multiplica por 2")
                        saldo_global += dinero_apostado
                    else:
                        print("Pierde lo apostado")
                        saldo_global -= dinero_apostado
                elif eleccion_ruleta == "3":
                    if saldo_global < APUESTA_MINIMA_RULETA:
                        print(
                            f"Necesitas al menos {APUESTA_MINIMA_RULETA} pesos para jugar a la ruleta")
                        break
                    paridad_eleccion_usuario = input(
                        "1. Par\n2. Impar\nElige: ")
                    if paridad_eleccion_usuario == "1":
                        paridad_usuario = PAR
                    else:
                        paridad_usuario = IMPAR
                    numero_aleatorio = random.randint(1, 20)
                    print("Número obtenido: " + str(numero_aleatorio))
                    if numero_aleatorio % 2 == 0 and paridad_usuario == PAR:
                        print("El número es par")
                        print(f"Gana {DINERO_GANADO_PARIDAD} pesos")
                        saldo_global += DINERO_GANADO_PARIDAD - dinero_apostado
                    elif numero_aleatorio % 2 != 0 and paridad_usuario == IMPAR:
                        print("El número es impar")
                        print(f"Gana {DINERO_GANADO_PARIDAD} pesos")
                        saldo_global += DINERO_GANADO_PARIDAD - dinero_apostado
                    else:
                        saldo_global -= dinero_apostado
                        print("Pierde la apuesta")
    print(f"Saldo final: {saldo_global}")


main()