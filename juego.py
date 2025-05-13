import sys
import random

def validacion(jugada_humano, jugada_pc): #para comparar las jugadas de las rondas
    reglas = {
        "piedra": {"tijera": 1, "papel": -1, "piedra": 0},
        "papel": {"piedra": 1, "tijera": -1, "papel": 0},
        "tijera": {"papel": 1, "piedra": -1, "tijera": 0}
    }
    return reglas[jugada_humano][jugada_pc]

def pedir_jugada(numero):
    print(f"Ingrese su jugada #{numero} (piedra, papel o tijera):")
    jugada = input().lower()

    while jugada != "piedra" and jugada != "papel" and jugada != "tijera":
        print("Entrada no válida. Debe escribir piedra, papel o tijera.")
        print(f"Intente nuevamente su jugada #{numero}:")
        jugada = input().lower()

    return jugada

def main():
    print("Bienvenido al juego de Piedra, Papel o Tijeras")
    print("Vas a jugar 3 rondas contra la computadora.\n")

    if len(sys.argv) == 4:
        jugadas_humano = [arg.lower() for arg in sys.argv[1:]]
        for jugada in jugadas_humano:
            if jugada not in ["piedra", "papel", "tijera"]:
                print(f"Jugada inválida: {jugada}")
                return
    else:
        print("Vas a jugar 3 rondas contra la computadora.\n")
        jugadas_humano = [
            pedir_jugada(1),
            pedir_jugada(2),
            pedir_jugada(3)
        ]

    # jugadas aleatorias para la maquina
    jugadas_pc = []
    jugadas_pc.append(random.choice(["piedra", "papel", "tijera"]))
    jugadas_pc.append(random.choice(["piedra", "papel", "tijera"]))
    jugadas_pc.append(random.choice(["piedra", "papel", "tijera"]))

    print("\nEl programa elige:", jugadas_pc[0], jugadas_pc[1], jugadas_pc[2])

    puntos_humano = 0
    puntos_pc = 0

    # Ronda 1
    resultado_1 = validacion(jugadas_humano[0], jugadas_pc[0])
    if resultado_1 == 1:
        puntos_humano += 1
    elif resultado_1 == -1:
        puntos_pc += 1

    # Ronda 2
    resultado_2 = validacion(jugadas_humano[1], jugadas_pc[1])
    if resultado_2 == 1:
        puntos_humano += 1
    elif resultado_2 == -1:
        puntos_pc += 1

    # Ronda 3
    resultado_3 = validacion(jugadas_humano[2], jugadas_pc[2])
    if resultado_3 == 1:
        puntos_humano += 1
    elif resultado_3 == -1:
        puntos_pc += 1

    # Resultado final
    print(f"\nPunteo: {puntos_humano} – {puntos_pc}")
    if puntos_humano > puntos_pc:
        print("Ganador: Humano")
    elif puntos_pc > puntos_humano:
        print("Ganador: Programa")
    else:
        print("Resultado: Empate")

main()