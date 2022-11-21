from random import randrange

def display_board(board):
    for x in range(3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|   " + board[x][0] + "   |   " + board[x][1] + "   |   " + board[x][2] + "   |")
        print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
    
    try:        
        mov_correcto = False
        while not(mov_correcto):
            x=0
            y=0
            #limpiamos siempre para evitar problemas
            movimiento_usu = input("Ingresa tu movimiento(inserta V para ver el tablero): ")
            if(movimiento_usu.upper() == "V"):
                display_board(board)
            else:    
                for x in range(3):
                    for y in range(3):
                        if board[x][y] == movimiento_usu:
                            mov_correcto = True
                            board[x][y] = "O"
                if mov_correcto == False:
                    print("El movimiento introducido no es valido")          
        
    except:
        print("no es un movimiento valido.")
        movimiento = enter_move()

def victory_for(board):
    
    x=0
    y=0
    winner = " "
    #primero reviso las filas:
    for x in range(3):
        if(board[x][0] == board[x][1] == board[x][2]):
            winner = board[x][0]
    #luego las columnas
    for y in range(3):
        if(board[0][y] == board[1][y] == board[2][y]):
            winner = board[0][y]
    #luego las diagonales
    if(board[0][0] == board[1][1] == board[2][2]):
        winner = board[1][1]
    if(board[0][2] == board[1][1] == board[2][0]):
        winner = board[1][1]

    return winner


def draw_move(board):
    
    mov_correcto = False

    while not(mov_correcto):
        x=0
        y=0
        #limpiamos siempre para evitar problemas
        mov_maquina = randrange(9)
        for x in range(3):
            for y in range(3):
                if board[x][y] == str(mov_maquina):
                    mov_correcto = True
                    board[x][y] = "X"
                    

board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
fin = False

while(fin != True):
    draw_move(board)
    ganador = victory_for(board) #tenemos que verificar si se ha acabado la partida despues de cada jugada
    if(ganador == " "):
        display_board(board)
        enter_move(board)
        ganador = victory_for(board)
    if(ganador != " "):
        fin = True
display_board(board)
print("La partida la gana las", ganador)
    

