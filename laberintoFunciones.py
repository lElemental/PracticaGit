FILAS = 5
COLUMNAS = 5
META_FILA = FILAS - 1
META_COLUMNA = COLUMNAS - 1

def inicializar_laberinto():
    """Crea el laberinto con la meta configurada."""
    laberinto = [[False] * COLUMNAS for _ in range(FILAS)]
    laberinto[META_FILA][META_COLUMNA] = True  # Meta
    return laberinto

def imprimir_laberinto(laberinto, fila_jugador, columna_jugador):
    """Imprime el laberinto con la posición del jugador."""
    for i in range(FILAS):
        for j in range(COLUMNAS):
            if i == fila_jugador and j == columna_jugador:
                print("X ", end="")  # Jugador
            elif laberinto[i][j]:
                print("O ", end="")  # Meta
            else:
                print(". ", end="")  # Espacio vacío
        print()

def mover_jugador(movimiento, fila_jugador, columna_jugador):
    """Actualiza la posición del jugador según el movimiento."""
    if movimiento == 's' and fila_jugador > 0:
        fila_jugador -= 1
    elif movimiento == 'x' and fila_jugador < FILAS - 1:
        fila_jugador += 1
    elif movimiento == 'z' and columna_jugador > 0:
        columna_jugador -= 1
    elif movimiento == 'c' and columna_jugador < COLUMNAS - 1:
        columna_jugador += 1
    else:
        print("Movimiento no válido.")
    return fila_jugador, columna_jugador

def main():
    laberinto = inicializar_laberinto()
    fila_jugador, columna_jugador = 0, 0

    while True:
        imprimir_laberinto(laberinto, fila_jugador, columna_jugador)

        if fila_jugador == META_FILA and columna_jugador == META_COLUMNA:
            print("\n¡Has alcanzado la meta! ¡Felicidades!")
            break

        movimiento = input("\nIngrese movimiento (s: arriba, x: abajo, z: izq, c: der): ")
        fila_jugador, columna_jugador = mover_jugador(movimiento, fila_jugador, columna_jugador)

if __name__ == "__main__":
    main()

    #Hola 123 
