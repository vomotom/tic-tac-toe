import os
from random import randint

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def board_init():
    board = []
    for i in range(9):
        board.append(i + 1)
    return board

def draw_board(board):
    horizontal_line = 3 * (" "+ "-" * 3)
    lines = []
    index_counter = 0
    for i in range(3):
        lines.append("|")
        for j in range(3):
            lines[i] += f" {board[index_counter]} |"
            index_counter += 1
    drawn_board = ""
    for i in range(3):
        drawn_board += horizontal_line + "\n" + lines[i] + "\n"
    drawn_board += horizontal_line
    print(drawn_board)

def player_turn(player, board):
    while True:
        player_input = input(f"(Hrac {player}) Na ktere pole chces tahnout? ")
        if player_input == "X" or player_input == "O":
            print(f"{player_input} neni platne pole. Zkus znovu...")
            continue
        try:   
            player_input = int(player_input)
            if player_input in board:
                break
            print(f"{player_input} neni platne pole. Zkus znovu...")
        except:
            print(f"{player_input} neni platne pole. Zkus znovu...")
    board[player_input - 1] = player

def computer_turn(board):
    eligible_moves = []
    for square in board:
        if type(square) == int:
            eligible_moves.append(square)
    move = eligible_moves[randint(0,len(eligible_moves)-1)]
    board[move - 1] = "O"

def check_state(board):
    lines = [
            (1,2,3),
            (4,5,6),
            (7,8,9),
            (1,4,7),
            (2,5,8),
            (3,6,9),
            (1,5,9),
            (3,5,7)
    ]
    for player in ["O", "X"]:
        for line in lines:
            win = False
            for square in line:
                if board[square-1] == player:
                    win = True
                else:
                    win = False
                    break
            if win == True:
                return player
    tie = True
    for line in lines:
        players_in_line = []
        for square in line:
            players_in_line.append(board[square-1])
        if "O" not in players_in_line or "X" not in players_in_line:
            tie = False
            break
    if tie:
        return "Tie"
    else:
        return False
                


board = board_init()
while True:
    clearConsole()
    draw_board(board)
    player_turn("X", board)
    state = check_state(board)
    if state:
        clearConsole()
        draw_board(board)
        if state == "Tie":
            print("Hru nelze vyhrat, konci remizou!")
        else:
            print(f"Hrac {state} vyhral!")
        break
    computer_turn(board)
    state = check_state(board)
    if state:
        clearConsole()
        draw_board(board)
        if state == "Tie":
            print("Hru nelze vyhrat, konci remizou!")
        else:
            print(f"Hrac {state} vyhral!")
        break
input()





