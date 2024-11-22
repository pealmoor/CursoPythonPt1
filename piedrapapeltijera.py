opciones = ["piedra", "papel", "tijera"]

print("Jugador 1: Elige piedra, papel o tijera.")
jugador1 = input(">> ").lower()

print("Jugador 2: Elige piedra, papel o tijera.")
jugador2 = input(">> ").lower()

# Validar entradas
if jugador1 not in opciones or jugador2 not in opciones:
    print("Una de las elecciones no es válida. Inténtalo de nuevo.")
else:
    # Mostrar elecciones
    print(f"Jugador 1 eligió: {jugador1}")
    print(f"Jugador 2 eligió: {jugador2}")

    # Determinar el resultado
    if jugador1 == jugador2:
        print("¡Es un empate!")
    elif (jugador1 == "piedra" and jugador2 == "tijera") or \
         (jugador1 == "papel" and jugador2 == "piedra") or \
         (jugador1 == "tijera" and jugador2 == "papel"):
        print("¡Jugador 1 gana!")
    else:
        print("¡Jugador 2 gana!")
