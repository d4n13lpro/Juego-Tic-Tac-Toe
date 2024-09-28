from random import randrange

# Función para mostrar el tablero
def display_board(board):
    for row in board:
        print("+-------" * 3 + "+")
        print("|       " * 3 + "|")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       " * 3 + "|")
    print("+-------" * 3 + "+")

# Función para capturar el movimiento del jugador
def enter_move(board):
    while True:
        try:
            move = int(input("Ingresa tu movimiento: "))
            if move in range(1, 10):
                for i, row in enumerate(board):
                    if move in row:
                        row[row.index(move)] = 'O'
                        return
            print("Movimiento inválido, intenta de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

# Función para generar una lista de campos vacíos
def make_list_of_free_fields(board):
    free_fields = []
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if isinstance(cell, int):
                free_fields.append((i, j))
    return free_fields

# Función para verificar si hay un ganador
def victory_for(board, sign):
    winning_combinations = [
        [(0, 0), (0, 1), (0, 2)], # filas
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)], # columnas
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)], # diagonales
        [(0, 2), (1, 1), (2, 0)]
    ]
    for combo in winning_combinations:
        if all(board[i][j] == sign for i, j in combo):
            return True
    return False

# Función para el movimiento de la máquina
def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        i, j = free_fields[randrange(len(free_fields))]
        board[i][j] = 'X'
