"""
Word Guessing Game - Detailed Documentation

This script implements a multiplayer word guessing game using words from a JSON file.

1. Import Statements
"""
import argparse
import json

"""
2. Input Validation Function

This function ensures that user input is a positive integer.
"""
def get_valid_integer_input(prompt):
    """
    Prompts for and validates a positive integer input.
    
    Args:
    prompt (str): The input to be converted to a positive integer

    Returns:
    int: A positive integer

    Continuously prompts the user until a valid positive integer is entered.
    """
    while True:
        try:
            value = int(prompt)
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except Exception:
            print("Please enter a valid number.")

"""
3. Command-line Argument Parsing

Sets up the argument parser to handle command-line inputs.
"""
parser = argparse.ArgumentParser(description="guessing words")
parser.add_argument("words_file", type=str, help="path to the file containing the list of words")
parser.add_argument("num_players", type=str, help="the number of players")
parser.add_argument("num_words", type=str, help="the number of words")
args = parser.parse_args()

"""
4. Word Loading

Loads words from the specified JSON file into a dictionary.
"""
with open(args.words_file, 'r', encoding='utf-8') as words:
    words_dict = json.load(words)

"""
5. Word Bank Creation

Creates a set of unique words from all categories in the loaded dictionary.
"""
words_bank = {word.lower() for words_list in words_dict.values() for word in words_list}
lengh_of_bank = len(words_bank)

"""
6. Game Setup

Initializes game parameters and collects player information.
"""
print("\nWelcome to the craziest guessing game in the universe!!\n")
number_of_words = lengh_of_bank + 1
while number_of_words > lengh_of_bank:
    number_of_words = get_valid_integer_input(args.num_words)

number_of_players = get_valid_integer_input(args.num_players)
players = [input(f"\nEnter name for player No. {i + 1}: \n") for i in range(number_of_players)]
scores = [0] * number_of_players
game_number = 1
index_player = -1

"""
7. Main Game Loop

Manages the overall flow of the game, selecting words and running guessing rounds.
"""
while words_bank and game_number <= number_of_words:
    random_word = words_bank.pop()

    # Find the category (hint) for the chosen word
    for key, value_list in words_dict.items():
        if random_word in value_list:
            hint = key
            break

    print(f"Game No. {game_number}:\n")
    print(f"The category of the word is: {hint}")

    word_progress = ["_"] * len(random_word)
    used_letters = set()
    print(' '.join(word_progress))

    """
    8. Word Guessing Loop

    Manages individual letter guesses for each word.
    """
    while '_' in word_progress:
        index_player = (index_player + 1) % number_of_players
        letter = input(f"\n{players[index_player]} enter letter:\n").lower()

        if (len(letter) == 1) and (letter not in used_letters):
            if letter in random_word:
                print("Great, you did it! :-)\n")
                for i, char in enumerate(random_word):
                    if char == letter:
                        word_progress[i] = letter
                        scores[index_player] += 1
            else:
                print("Sorry, but you were wrong :-(\n")

            used_letters.add(letter)
        else:
            print("\nMore than one letter has been entered or this character has already been detected.\n")
            index_player -= 1
        
        print(f"{' '.join(word_progress)}\nLetters already guessed: {", ".join(sorted(used_letters))}")

    print(f"Game No. {game_number} successfully completed. The word was: {random_word.capitalize()}\n")
    game_number += 1

"""
9. Game Conclusion

Announces the end of the game and determines the winner(s).
"""
print("\nGame Over!!\n")
high_score = max(scores)
if scores.count(high_score) == 1:
    print(f"The winner player is: {players[scores.index(high_score)]}, with {high_score} points.")
else:
    print(f"The winners players is: {",".join([players[i] for i in range(number_of_players) if scores[i] == high_score])} with {high_score} points.")