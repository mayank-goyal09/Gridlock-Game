import numpy as np
import random
import time

# --- SETUP ---
def create_grid():
    return np.full((3, 3), ' ', dtype='<U1')

def check_winner(board, player):
    for row in board:
        if np.all(row == player): return True
    for col in board.T:
        if np.all(col == player): return True
    if np.all(np.diag(board) == player): return True
    if np.all(np.diag(np.fliplr(board)) == player): return True
    return False

def is_board_full(board):
    return np.all(board != ' ')

def get_computer_move(board):
    empty_spots = np.argwhere(board == ' ')
    if len(empty_spots) > 0:
        return random.choice(empty_spots)
    return None

# --- GAME LOOP ---
def play_vs_computer():
    board = create_grid()
    human = 'X'
    computer = 'O'
    current_player = human # Human starts
    
    print("🤖 GRIDLOCK: Human vs. Computer")
    print("--------------------------------")
    print(board)
    
    while True:
        print(f"\n👉 Player {current_player}'s Turn")
        
        if current_player == human:
            # --- HUMAN TURN ---
            try:
                r = int(input("Row (0-2): "))
                c = int(input("Col (0-2): "))
            except ValueError:
                print("⚠️ Invalid input.")
                continue

            if r not in range(3) or c not in range(3):
                print("🚫 Out of bounds.")
                continue
            if board[r, c] != ' ':
                print("🚫 Spot taken.")
                continue
                
        else:
            # --- COMPUTER TURN ---
            print("Thinking... 💭")
            time.sleep(1) # Add a small delay to make it feel real
            move = get_computer_move(board)
            if move is None: break # Should be caught by draw check, but just in case
            r, c = move
            print(f"🤖 Computer chose ({r}, {c})")

        # Execute Move
        board[r, c] = current_player
        print(board)

        # Check Win
        if check_winner(board, current_player):
            winner = "YOU" if current_player == human else "COMPUTER"
            print(f"\n🏆 GAME OVER! {winner} WIN! 🏆")
            break

        # Check Draw
        if is_board_full(board):
            print("\n🤝 It's a DRAW!")
            break

        # Switch
        current_player = computer if current_player == human else human

# Let's play!
play_vs_computer()
