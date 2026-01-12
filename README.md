# ⚡ GRIDLOCK // ZERO_SUM

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/Powered%20By-NumPy-013243.svg)](https://numpy.org/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Gridlock** is a high-performance Tic-Tac-Toe engine that demonstrates the power of **NumPy** for game state management, win-condition validation through vectorized operations, and AI decision-making.

🔗 **[Play the Live Demo](https://gridlock-game-bdoqnt2uavckvypewafl8g.streamlit.app/)**

---


## 🚀 Project Overview

Gridlock transcends the basic "if-else" Tic-Tac-Toe logic. By representing the 3x3 board as a **2D NumPy NDArray**, the game utilizes mathematical properties to detect wins and calculate AI moves. 

### Key Features
- **Vectorized Win Detection**: Uses `np.trace()`, `np.sum()`, and slicing rather than nested loops.
- **Smart AI**: Features three difficulty levels, including a "Smart" mode powered by the **Minimax Algorithm**.
- **Monte Carlo Simulations**: A built-in simulator that runs up to 5,000 games in seconds to analyze win/loss probabilities using NumPy's speed.
- **Interactive UI**: A sleek Streamlit interface for seamless browser-based play.

---

## 🛠️ Tech Stack & Skills

| Category | Technologies / Concepts |
| :--- | :--- |
| **Core** | Python 3.x, NumPy |
| **Frontend** | Streamlit |
| **Algorithms** | Minimax (Decision Trees), Monte Carlo Simulation |
| **NumPy Skills** | Broadcasting, Boolean Masking, Trace/Diagonal Operations, Slicing |

---

## 🧠 Technical Deep Dive

### 1. The NumPy Advantage
Instead of iterating through rows and columns to find a winner, Gridlock treats the board as a matrix $M$. 
- **Rows/Cols**: `np.sum(board, axis=0)` and `np.sum(board, axis=1)`
- **Diagonals**: `board.diagonal()` and `np.fliplr(board).diagonal()`
This allows for near-instant win validation even during heavy Monte Carlo simulations.

### 2. AI Logic
- **Easy**: Random sampling of available indices.
- **Medium**: Heuristic-based moves.
- **Smart**: A recursive Minimax algorithm that ensures the AI never loses.

---

## 📂 Project Structure

```text
Gridlock Game/
├── main.py           # CLI entry point
├── app.py            # Streamlit UI implementation
├── engine.py         # The NumPy-powered game core
├── app_structure.py  # Architectural helper functions
├── grid_game.ipynb   # Interactive tutorial & logic breakdown
├── requirements.txt  # Dependencies (numpy, streamlit)
└── README.md         # Professional documentation

```

---

## ⚙️ Installation & Usage

1. **Clone the repository**
```bash
git clone https://github.com/mayank-goyal09/nothing.git
cd gridlock-game

```


2. **Install dependencies**
```bash
pip install -r requirements.txt

```


3. **Run the Web App**
```bash
streamlit run app.py

```


4. **Run the CLI Version**
```bash
python main.py

```



---

## 📊 Monte Carlo Insights

The project includes a simulation module. By running thousands of randomized games, users can visualize the statistical likelihood of a "Draw" vs. a "Win" based on different starting positions, demonstrating the mathematical balance of the game.

---

## ✍️ Author

**Mayank Goyal** *Course: Exercise 4 - NumPy and Python Logic Building* *Date: November 2025*

---

⭐ *If you find this project helpful for learning NumPy, feel free to give it a star!*
