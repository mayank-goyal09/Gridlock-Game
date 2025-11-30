import streamlit as st
import time
import numpy as np
import matplotlib.pyplot as plt
import main as engine  # Importing your backend logic

st.set_page_config(page_title="Gridlock AI", page_icon="🤖")

st.title("🎮 Gridlock: NumPy Edition")
st.caption("Frontend: Streamlit | Backend: main.py | Analysis: Monte Carlo")

# ==========================================
# 1. PLAYABLE GAME SECTION
# ==========================================

# --- Initialize Session State ---
if 'board' not in st.session_state:
    st.session_state.board = engine.create_grid()
    st.session_state.turn = 'X'
    st.session_state.winner = None
    st.session_state.game_over = False

def reset_game():
    st.session_state.board = engine.create_grid()
    st.session_state.turn = 'X'
    st.session_state.winner = None
    st.session_state.game_over = False

def handle_move(r, c):
    if st.session_state.board[r, c] == ' ' and not st.session_state.game_over:
        st.session_state.board[r, c] = 'X'
        
        if engine.check_winner(st.session_state.board, 'X'):
            st.session_state.winner = "You (X)"
            st.session_state.game_over = True
        elif engine.is_board_full(st.session_state.board):
            st.session_state.winner = "Draw"
            st.session_state.game_over = True
        else:
            st.session_state.turn = 'O'
            computer_turn()

def computer_turn():
    if not st.session_state.game_over:
        with st.spinner("Thinking..."):
            time.sleep(0.2)
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

# --- GAME UI ---
col1, col2 = st.columns([2, 1])

with col1:
    # Display Game Status
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

    # Draw Grid
    for r in range(3):
        cols = st.columns(3)
        for c in range(3):
            cell = st.session_state.board[r, c]
            if cell == ' ':
                cols[c].button(" ", key=f"{r}-{c}", on_click=handle_move, args=(r, c), disabled=st.session_state.game_over)
            else:
                cols[c].button(cell, key=f"{r}-{c}", disabled=True)

# ==========================================
# 2. DATA SCIENCE SIDEBAR (The Simulation)
# ==========================================

with st.sidebar:
    st.header("📊 Data Analysis")
    st.markdown("Check the fairness of the game by running a **Monte Carlo Simulation**.")
    
    num_sims = st.slider("Number of Games", 100, 2000, 1000)
    
    if st.button("🚀 Run Simulation"):
        progress_bar = st.progress(0)
        results = []
        
        # --- SIMULATION LOOP (Using main.py logic) ---
        for i in range(num_sims):
            # Run one silent game
            sim_board = engine.create_grid()
            sim_turn = 'X'
            sim_winner = None
            
            while True:
                move = engine.get_computer_move(sim_board)
                if move is None: 
                    sim_winner = "Draw"
                    break
                
                sim_board[tuple(move)] = sim_turn
                
                if engine.check_winner(sim_board, sim_turn):
                    sim_winner = sim_turn
                    break
                if engine.is_board_full(sim_board):
                    sim_winner = "Draw"
                    break
                
                sim_turn = 'O' if sim_turn == 'X' else 'X'
            
            results.append(sim_winner)
            
            # Update progress bar every 10%
            if i % (num_sims // 10) == 0:
                progress_bar.progress((i + 1) / num_sims)
        
        progress_bar.progress(100)
        
        # --- VISUALIZE RESULTS ---
        x_wins = results.count('X')
        o_wins = results.count('O')
        draws = results.count('Draw')
        
        st.success(f"Simulated {num_sims} games!")
        
        # Create Matplotlib Chart
        fig, ax = plt.subplots()
        labels = ['Player X', 'Player O', 'Draws']
        counts = [x_wins, o_wins, draws]
        colors = ['#3498db', '#e74c3c', '#95a5a6']
        
        ax.bar(labels, counts, color=colors)
        ax.set_ylabel("Wins")
        ax.set_title(f"First Mover Advantage (n={num_sims})")
        
        # Add labels on bars
        for i, v in enumerate(counts):
            ax.text(i, v + 10, str(v), ha='center', fontweight='bold')
            
        st.pyplot(fig)
        
        st.write(f"**Player X Win Rate:** {(x_wins/num_sims)*100:.1f}%")
        st.write(f"**Player O Win Rate:** {(o_wins/num_sims)*100:.1f}%")
