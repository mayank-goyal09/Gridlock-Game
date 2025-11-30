import streamlit as st
import time
# 👇 HERE IS THE MAGIC
import main as engine 

st.title("🎮 Gridlock: NumPy Edition")
st.caption("Frontend: Streamlit | Backend: main.py")

# --- Initialize Session State ---
if 'board' not in st.session_state:
    st.session_state.board = engine.create_grid() # Calls main.py
    st.session_state.turn = 'X'
    st.session_state.winner = None
    st.session_state.game_over = False

# --- Reset Function ---
def reset_game():
    st.session_state.board = engine.create_grid() # Calls main.py
    st.session_state.turn = 'X'
    st.session_state.winner = None
    st.session_state.game_over = False

# --- Move Logic ---
def handle_move(r, c):
    # 1. Human Move
    if st.session_state.board[r, c] == ' ' and not st.session_state.game_over:
        st.session_state.board[r, c] = 'X'
        
        # Check Human Win using engine
        if engine.check_winner(st.session_state.board, 'X'):
            st.session_state.winner = "You (X)"
            st.session_state.game_over = True
        elif engine.is_board_full(st.session_state.board):
            st.session_state.winner = "Draw"
            st.session_state.game_over = True
        else:
            # 2. Computer Move
            st.session_state.turn = 'O'
            computer_turn()

def computer_turn():
    if not st.session_state.game_over:
        with st.spinner("Thinking..."):
            time.sleep(0.3)
            # Calls main.py for the move!
            move = engine.get_computer_move(st.session_state.board)
            
            if move is not None:
                st.session_state.board[tuple(move)] = 'O'
                
                if engine.check_winner(st.session_state.board, 'O'):
                    st.session_state.winner = "Computer (O)"
                    st.session_state.game_over = True
                elif engine.is_board_full(st.session_state.board):
                    st.session_state.winner = "Draw"
                    st.session_state.game_over = True
            
            st.session_state.turn = 'X'

# --- UI LAYOUT ---
if st.session_state.game_over:
    if st.session_state.winner == "Draw":
        st.warning("🤝 It's a Draw!")
    elif st.session_state.winner == "You (X)":
        st.success("🏆 YOU WON!")
        st.balloons()
    else:
        st.error("🤖 Computer Won!")
    
    st.button("Play Again 🔄", on_click=reset_game)
else:
    st.info(f"Current Turn: {st.session_state.turn}")

# Render Grid
for r in range(3):
    cols = st.columns(3)
    for c in range(3):
        cell_value = st.session_state.board[r, c]
        if cell_value == ' ':
            cols[c].button(" ", key=f"{r}-{c}", on_click=handle_move, args=(r, c), disabled=st.session_state.game_over)
        else:
            cols[c].button(cell_value, key=f"{r}-{c}", disabled=True)
