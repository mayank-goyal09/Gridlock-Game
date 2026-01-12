# Gridlock Game
https://gridlock-game-bdoqnt2uavckvypewafl8g.streamlit.app/
🎮 A NumPy powered Tic Tac Toe style game that demonstrates advanced array manipulation, logical operations, and Python game logic design.

## Project Overview

Gridlock is an interactive 3x3 grid game where two players take turns marking their positions. This project showcases practical applications of NumPy arrays for game development, decision logic, and win condition validation.

## About This Project

**Course:** Exercise 4  
**Topic Covered:** NumPy and Python Logic Building  
**Difficulty Level:** Intermediate

## Project Description

Develop a Tic Tac Toe style game named Gridlock, powered by NumPy. The game simulates a 3x3 grid where two players take turns marking their positions. The implementation uses NumPy arrays to represent the grid, handle player moves, and check for winning conditions such as rows, columns, or diagonals. The game incorporates logic for detecting invalid moves and draws, ensuring smooth gameplay through conditionals and loops.

## Skills Covered

✓ NumPy array manipulation and indexing  
✓ Logical operations and boolean masking  
✓ Control flow with conditionals  
✓ Loop structures and iteration  
✓ Conditional statements and branching  
✓ Game logic design and implementation  
✓ Input validation and error handling  
✓ Win condition detection algorithms

## What I Learned

### NumPy Concepts

• Creating and manipulating 2D arrays for grid representation  
• Using NumPy operations for efficient game state checking  
• Leveraging array broadcasting for win condition validation  
• Implementing vectorized operations for game logic  

### Programming Fundamentals

• Designing game flow with conditional logic  
• Implementing nested loops for board traversal  
• Validating user input and handling edge cases  
• Structuring code for maintainability and clarity  

### Problem Solving

• Detecting winning patterns across rows, columns, and diagonals  
• Implementing move validation to prevent overlapping positions  
• Designing algorithms to check game draw conditions  
• Managing game state transitions effectively  

## Project Structure

```
Gridlock Game/
├── main.py              # Game entry point and main loop
├── app.py               # Application interface
├── app_structure.py     # Game structure and architecture
├── grid_game.ipynb      # Jupyter notebook with detailed explanations
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

## Files Description

**main.py** - Core game logic and player turn management  
**app.py** - User interface and game display  
**app_structure.py** - Game architecture and helper functions  
**grid_game.ipynb** - Detailed explanations with step by step game logic and NumPy array manipulation concepts

## Learning Resources

📚 **[View Practice Notebook](https://github.com/mayank-goyal09/nothing/blob/main/grid_game.ipynb)** - Comprehensive documentation with detailed explanations, NumPy concepts, and step by step logic building

## Technologies Used

• Python 3.x  
• NumPy  

## How to Run

1. Install dependencies  
   ```bash
   pip install numpy
   ```

2. Run the game  
   ```bash
   python main.py
   ```

## Key Takeaways

This project reinforced the importance of efficient data structures like NumPy arrays for game development. Through building Gridlock, I gained practical experience in implementing complex game logic, understanding win condition algorithms, and writing clean, maintainable Python code. The experience highlighted how mathematical operations and array manipulation can elegantly solve game logic problems.

---

## 🎮 Live Demo

**Play the game live here:** [Gridlock: NumPy Edition](https://gridlock-game-bdoqnt2uavckvypewafl8g.streamlit.app/)

This interactive Streamlit app brings Gridlock to life with:

### Features

- **Interactive Gameplay**: Play against AI with multiple difficulty levels (Easy, Medium, Smart)
- **Real-time Board Display**: Visual 3x3 grid showing current game state
- **Score Tracking**: Keep track of wins, losses, and draws across multiple rounds
- **AI Difficulty Levels**:
  - **Easy**: Random moves
  - **Medium**: Mixed strategy with some intelligent moves
  - **Smart**: Optimal minimax algorithm for unbeatable gameplay
- **Monte Carlo Simulations**: Run statistical analysis on game outcomes with configurable simulation counts (100-5000 games)
- **Game Reset Options**:
  - New Round: Start fresh while keeping scores
  - Reset Score: Clear all statistics

### Tech Stack

- **Frontend**: Streamlit for interactive UI
- **Backend**: NumPy-powered game engine (`engine.py`)
- **AI Algorithm**: Minimax decision tree for optimal play
- **Analysis**: Monte Carlo simulation for win/draw probability analysis

---

**Author:** Mayank Goyal  
**Date:** November 2025
