from random import randrange


board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]



def display_board(board):
    for x in range(3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|   " + board[x][0] + "   |   " + board[x][1] + "   |   " + board[x][2] + "   |")
        print("|       |       |       |")
print("+-------+-------+-------+")


def enter_move(board):
    try:
        movimiento = input("Ingresa tu movimiento: ")
    except:
        print("no es un movimiento valido.")
        print("selecciona una de las celdas vacias: ")
        movimiento = enter_move()
    return movimiento


def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.


def victory_for(board, sign):
    # La función analiza el estatus del tablero para verificar si 
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.


def draw_move(board):
    
    mov_correcto = False

    while not(mov_correcto):
        mov_maquina = randrange(9)
        for x in range(3):
            for y in range(3):
                if board[x,y] == mov_maquina:
                    mov_correcto = True
                    board[x,y] = "X"
                    




