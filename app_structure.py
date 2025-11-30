import numpy as np
import random

# --- PURE LOGIC FUNCTIONS ---
def create_grid():
    return np.full((3, 3), ' ', dtype='<U1')

def check_winner(board, player):
    if np.any(np.all(board == player, axis=1)): return True
    if np.any(np.all(board == player, axis=0)): return True
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
