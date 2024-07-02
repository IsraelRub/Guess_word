
# Word Guessing Game

This Python script implements an interactive multiplayer word guessing game. Players take turns guessing letters to reveal hidden words, competing to score the most points.

## Features

- Supports multiple players
- Loads words from a JSON file, organized by categories
- Provides hints for each word based on its category
- Tracks player scores and determines winner(s)
- Handles input validation for game setup and letter guessing

## How to Play

1. Run the script with the required arguments:
   python word_guessing_game.py <words_file> <num_players> <num_words>
   - words_file: Path to JSON file containing categorized words
   - num_players: Number of players
   - num_words: Number of words to guess

2. Enter names for each player when prompted.

3. For each round:
   - A word is randomly selected, and its category is shown as a hint.
   - Players take turns guessing letters.
   - Correct guesses reveal the letter in the word and award points.
   - The game continues until the word is fully revealed.

4. After all rounds, the winner(s) with the highest score are announced.

## Requirements

- Python 3.x
- JSON file with categorized words (sample format provided in repository)

## Installation

1. Clone this repository:
   git clone https://github.com/yourusername/word-guessing-game.git

2. Navigate to the project directory:
   cd word-guessing-game

3. Run the game (see "How to Play" section).
