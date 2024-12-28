import random

def print_board(board):
    print("  0   1   2")
    for idx, row in enumerate(board):
        print(idx, " | ".join(row))
        if idx < 2:
            print("  " + "-" * 9)

def check_winner(board, player):
    # Check rows, columns and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_board_full(board):
    return all([cell != " " for row in board for cell in row])

def get_computer_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_cells)

def get_player_names():
    player1 = input("Enter name for Player 1 (X): ")
    player2 = input("Enter name for Player 2 (O) or leave blank for computer: ")
    return player1, player2 if player2 else "Computer"

def get_game_settings():
    rounds = int(input("Enter the number of rounds: "))
    move_limit = int(input("Enter the move limit per player: "))
    mode = input("Select mode: 1 for 2-player, 2 for play with computer: ")
    if mode not in ["1", "2"]:
        print("Invalid mode selected. Exiting.")
        exit()
    return rounds, move_limit, mode

def tic_tac_toe():
    player1, player2 = get_player_names()
    rounds, move_limit, mode = get_game_settings()
    
    scores = {player1: 0, player2: 0}
    
    for round_num in range(1, rounds + 1):
        print(f"Round {round_num}")
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = "X"
        move_count = 0
        
        while True:
            print_board(board)
            
            if mode == "2" and current_player == "O":
                row, col = get_computer_move(board)
                print(f"Computer chose: row {row}, column {col}")
            else:
                player_name = player1 if current_player == "X" else player2
                row = int(input(f"{player_name} ({current_player}), enter the row (0, 1, 2): "))
                col = int(input(f"{player_name} ({current_player}), enter the column (0, 1, 2): "))
            
            if board[row][col] != " ":
                print("Cell already taken, try again.")
                continue
            
            board[row][col] = current_player
            move_count += 1
            
            if check_winner(board, current_player):
                print_board(board)
                print(f"{player_name} ({current_player}) wins!")
                scores[player_name] += 1
                break
            
            if is_board_full(board) or move_count >= move_limit:
                print_board(board)
                print("It's a tie!")
                break
            
            current_player = "O" if current_player == "X" else "X"
        
        print(f"Scores: {player1} - {scores[player1]}, {player2} - {scores[player2]}")
        
        if round_num < rounds:
            rematch = input("Do you want a rematch? (yes/no): ").strip().lower()
            if rematch != "yes":
                break

    print("Final Scores:")
    print(f"{player1}: {scores[player1]}")
    print(f"{player2}: {scores[player2]}")
    print("Game Over")

if __name__ == "__main__":
    tic_tac_toe()
