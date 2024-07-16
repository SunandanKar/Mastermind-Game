# Mastermind Game in Python

## Overview
The Mastermind game is a classic code-breaking game where one player sets a secret 4-digit number, and the other player attempts to guess it within a limited number of tries. This project implements the Mastermind game in Python with a graphical user interface (GUI) using the tkinter library. It's a great exercise in logical thinking, pattern recognition, and GUI development.

## Features
- **Graphical User Interface:** Built using Python's tkinter library to create an interactive and user-friendly interface.
- **Two-Player Gameplay:** Players take turns being the code setter and the code breaker.
- **Color-Coded Feedback:** Immediate visual feedback on each guess:
  - **Blue:** Correct number but in the wrong position.
  - **Green:** Correct number in the correct position.
- **Limited Attempts:** Players have up to 5 attempts to guess the secret number, adding challenge and strategy.

## How It Works
1. **Initialization:**
   - The game starts with Player 1 setting a secret 4-digit number.
   - Player 2 attempts to guess the number within 5 attempts.

2. **Game Flow:**
   - **Player 1's Turn:**
     - Enters a 4-digit number as the secret code.
     - Clicks "Set Number" to confirm the code.

   - **Player 2's Turn:**
     - Enters a 4-digit guess into the input field.
     - Clicks "Guess" to submit the guess.
     - Receives immediate feedback in the table:
       - Numbers displayed in **blue** indicate correct numbers but in the wrong position.
       - Numbers displayed in **green** indicate correct numbers in the correct position.

   - **End of Game:**
     - If Player 2 correctly guesses the number within 5 attempts, a congratulatory message appears.
     - The game resets for a new round.

3. **Graphical Interface:**
   - Utilizes tkinter widgets for labels, buttons, text entries, and text display areas.
   - Implements scrollbars for the instructions and game history table for better user experience.

## Benefits and Learning
- **Python GUI Development:** Enhances skills in building graphical applications using tkinter.
- **Algorithmic Thinking:** Improves logical and strategic thinking through the game's code-breaking challenge.
- **User Interaction:** Provides a hands-on experience in creating interactive user interfaces in Python.

## Future Improvements
- Implementing a more sophisticated AI for automated code-breaking.
- Adding sound effects or animations to enhance user engagement.
- Enhancing the visual design for a more polished appearance.

## Get Started
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/mastermind-game.git
   ```
   
2. Install tkinter if not already installed:
   ```
   pip install tk
   ```

3. Run the game:
   ```
   python mastermind_game.py
   ```

## Contribution
Contributions are welcome! Feel free to fork the repository, make improvements, and submit pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
