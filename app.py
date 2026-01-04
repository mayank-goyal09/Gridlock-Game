import time
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

import app_structure as engine
  # renamed backend file: engine.py


st.set_page_config(
    page_title="Gridlock AI",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded",
)  # page config options are supported like this [web:3]


# ---------------------------
# Styling (fun + clean)
# ---------------------------
st.markdown(
    """
    <style>
    .block-container { padding-top: 1.5rem; }
    div[data-testid="stMetricValue"] { font-size: 1.4rem; }
    button[kind="secondary"] { border-radius: 14px; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🎮 Gridlock: NumPy Edition")
st.caption("Frontend: Streamlit | Backend: engine.py | Analysis: Monte Carlo")


# ---------------------------
# Session state
# ---------------------------
def init_state():
    if "board" not in st.session_state:
        st.session_state.board = engine.create_grid()
    if "turn" not in st.session_state:
        st.session_state.turn = "X"
    if "winner" not in st.session_state:
        st.session_state.winner = None
    if "game_over" not in st.session_state:
        st.session_state.game_over = False
    if "score" not in st.session_state:
        st.session_state.score = {"X": 0, "O": 0, "Draw": 0}
    if "difficulty" not in st.session_state:
        st.session_state.difficulty = "Smart"


def reset_round():
    st.session_state.board = engine.create_grid()
    st.session_state.turn = "X"
    st.session_state.winner = None
    st.session_state.game_over = False


init_state()


# ---------------------------
# Computer logic wrapper
# ---------------------------
def computer_choose_move(board: np.ndarray):
    # "Fun" difficulty: sometimes random, sometimes smart.
    if st.session_state.difficulty == "Chaotic":
        empties = np.argwhere(board == " ")
        if len(empties) == 0:
            return None
        return empties[np.random.randint(0, len(empties))]
    return engine.get_computer_move(board)


def finish_game(result):
    st.session_state.game_over = True
    st.session_state.winner = result
    if result == "X":
        st.session_state.score["X"] += 1
    elif result == "O":
        st.session_state.score["O"] += 1
    else:
        st.session_state.score["Draw"] += 1


def handle_move(r, c):
    if st.session_state.game_over:
        return

    if st.session_state.board[r, c] != " ":
        return

    # Player move
    st.session_state.board[r, c] = "X"

    if engine.check_winner(st.session_state.board, "X"):
        finish_game("X")
        return
    if engine.is_board_full(st.session_state.board):
        finish_game("Draw")
        return

    # Computer move
    st.session_state.turn = "O"
    with st.spinner("🤖 Thinking..."):
        time.sleep(0.15)
        move = computer_choose_move(st.session_state.board)

    if move is None:
        finish_game("Draw")
        st.session_state.turn = "X"
        return

    st.session_state.board[tuple(move)] = "O"

    if engine.check_winner(st.session_state.board, "O"):
        finish_game("O")
    elif engine.is_board_full(st.session_state.board):
        finish_game("Draw")

    st.session_state.turn = "X"


# ---------------------------
# Layout
# ---------------------------
left, right = st.columns([2.2, 1])

with right:
    st.subheader("⚙️ Controls")
    st.session_state.difficulty = st.selectbox(
        "Difficulty",
        ["Smart", "Chaotic"],
        index=["Smart", "Chaotic"].index(st.session_state.difficulty),
        help="Smart uses your engine logic. Chaotic plays random moves for memes 😎",
    )

    m1, m2, m3 = st.columns(3)
    m1.metric("X Wins", st.session_state.score["X"])
    m2.metric("O Wins", st.session_state.score["O"])
    m3.metric("Draws", st.session_state.score["Draw"])

    c1, c2 = st.columns(2)
    c1.button("🔄 New Round", use_container_width=True, on_click=reset_round)
    if c2.button("🧹 Reset Score", use_container_width=True):
        st.session_state.score = {"X": 0, "O": 0, "Draw": 0}

    st.divider()
    st.subheader("📊 Monte Carlo")
    st.write("Run simulations to see win/draw rates.")
    num_sims = st.slider("Number of games", 100, 5000, 1000, step=100)

    run = st.button("🚀 Run simulation", use_container_width=True)

with left:
    st.subheader("🧩 The Board")

    # Game status
    if st.session_state.game_over:
        if st.session_state.winner == "Draw":
            st.warning("🤝 It’s a draw. Respect.")
        elif st.session_state.winner == "X":
            st.success("🏆 You won! (humans still undefeated... sometimes)")
            st.balloons()
        else:
            st.error("🤖 Computer won. The machines are learning.")
        st.caption("Hit **New Round** to play again.")
    else:
        st.info(f"Current turn: {st.session_state.turn}")

    # Board UI (bigger buttons)
    for r in range(3):
        cols = st.columns(3)
        for c in range(3):
            cell = st.session_state.board[r, c]
            label = cell if cell != " " else "·"
            cols[c].button(
                label,
                key=f"cell-{r}-{c}",
                on_click=handle_move,
                args=(r, c),
                use_container_width=True,
                disabled=st.session_state.game_over or cell != " ",
            )

# ---------------------------
# Simulation
# ---------------------------
if run:
    progress = st.progress(0)
    results = {"X": 0, "O": 0, "Draw": 0}

    for i in range(num_sims):
        sim_board = engine.create_grid()
        sim_turn = "X"

        while True:
            move = computer_choose_move(sim_board)
            if move is None:
                results["Draw"] += 1
                break

            sim_board[tuple(move)] = sim_turn

            if engine.check_winner(sim_board, sim_turn):
                results[sim_turn] += 1
                break

            if engine.is_board_full(sim_board):
                results["Draw"] += 1
                break

            sim_turn = "O" if sim_turn == "X" else "X"

        # smooth progress (no division-by-zero edge cases)
        if (i + 1) % max(1, num_sims // 100) == 0:
            progress.progress((i + 1) / num_sims)

    progress.progress(1.0)
    st.success(f"Simulated {num_sims} games ✅")

    fig, ax = plt.subplots()
    labels = ["Player X", "Player O", "Draws"]
    counts = [results["X"], results["O"], results["Draw"]]
    ax.bar(labels, counts)
    ax.set_ylabel("Count")
    ax.set_title(f"Outcomes (n={num_sims})")

    for j, v in enumerate(counts):
        ax.text(j, v, str(v), ha="center", va="bottom")

    st.pyplot(fig)  # standard matplotlib rendering in Streamlit [web:1]

    st.write(f"**X Win Rate:** {(results['X']/num_sims)*100:.1f}%")
    st.write(f"**O Win Rate:** {(results['O']/num_sims)*100:.1f}%")
    st.write(f"**Draw Rate:** {(results['Draw']/num_sims)*100:.1f}%")
