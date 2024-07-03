# Rock-Paper-Scissors-Game
A simple console-based Rock, Paper, Scissors game implemented in Python with options to choose difficulty levels and persistent gameplay until the player chooses to change the difficulty or exit.

---

# Rock Paper Scissors Game with Dynamic Difficulty

This repository contains a Python implementation of the classic Rock, Paper, Scissors game, enhanced with a dynamic difficulty adjustment using a Markov Chain model. The game allows players to choose between different difficulty levels and continues at the chosen difficulty until the player decides to exit or change the difficulty level.

## Features

- **Dynamic Difficulty Levels**: Choose between `easy`, `normal`, and `hard` difficulty levels.
- **Markov Chain**: Difficulty transitions are modeled using a Markov Chain with customizable state transition probabilities.
- **Smart Computer Choices**: At higher difficulty levels, the computer makes smarter choices based on the player's previous moves.
- **Interactive Gameplay**: The game continues at the chosen difficulty level until the user decides to exit or change the difficulty.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/rock-paper-scissors-markov.git
    cd rock-paper-scissors-markov
    ```

2. Run the game:
    ```bash
    python3 rock_paper_scissors.py
    ```

## How to Play

1. **Choose Difficulty Level**: When prompted, choose the difficulty level by entering `easy`, `normal`, or `hard`. The game will continue at this difficulty level until you choose to exit or change the difficulty.

2. **Make Your Move**: Enter `R` for Rock, `P` for Paper, `S` for Scissors.

3. **Change Difficulty**: Enter `D` to change the difficulty level.

4. **Exit the Game**: Enter `E` to exit the game.

### Example Gameplay

```plaintext
Choose difficulty level ('easy', 'normal', 'hard'), 'E' to exit: easy
Current difficulty: easy
Enter 'R' for Rock, 'P' for Paper, 'S' for Scissors, 'D' to change difficulty, 'E' to exit: R
Computer chooses: Scissors
You win! Rock beats Scissors.
Score - Player: 1, Computer: 0, Ties: 0

Enter 'R' for Rock, 'P' for Paper, 'S' for Scissors, 'D' to change difficulty, 'E' to exit: P
Computer chooses: Rock
You win! Paper beats Rock.
Score - Player: 2, Computer: 0, Ties: 0

Enter 'R' for Rock, 'P' for Paper, 'S' for Scissors, 'D' to change difficulty, 'E' to exit: D
Choose new difficulty level ('easy', 'normal', 'hard'): hard
Current difficulty: hard
Enter 'R' for Rock, 'P' for Paper, 'S' for Scissors, 'D' to change difficulty, 'E' to exit: S
Computer chooses: Rock
You lose! Rock beats Scissors.
Score - Player: 2, Computer: 1, Ties: 0

Enter 'R' for Rock, 'P' for Paper, 'S' for Scissors, 'D' to change difficulty, 'E' to exit: E
Exiting the game.
Thanks for playing!
```

## Customization

### Adjusting Transition Probabilities

You can customize the state transition probabilities in the `MarkovChain` class. The `transition_probs` dictionary contains matrices for each difficulty level, defining the probabilities of transitioning to each state from the current state.

```python
self.transition_probs = {
    "easy": {"easy": [0.7, 0.2, 0.1], "normal": [0.6, 0.3, 0.1], "hard": [0.5, 0.3, 0.2]},
    "normal": {"easy": [0.3, 0.6, 0.1], "normal": [0.2, 0.7, 0.1], "hard": [0.1, 0.3, 0.6]},
    "hard": {"easy": [0.1, 0.2, 0.7], "normal": [0.1, 0.3, 0.6], "hard": [0.05, 0.15, 0.8]}
}
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.



