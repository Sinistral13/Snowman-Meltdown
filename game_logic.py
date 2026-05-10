import random
from ascii_art import STAGES
from pickle import FALSE

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def is_game_won(guessed_letters, secret_word):
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True    
    

def is_game_lost(mistakes):
    if mistakes == len(STAGES):
        return True
    return False


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    # For now, display the initial game state.
    display_game_state(mistakes, secret_word, guessed_letters)
    
    while True:
        # Prompt user for one guess (logic to be enhanced later)
        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)
    
        if guess in secret_word:
            guessed_letters.append(guess)
            if is_game_won(guessed_letters, secret_word):
                display_game_state(mistakes, secret_word, guessed_letters)
                print(f'GAME WON!')
                break
        else:
            mistakes += 1
            if is_game_lost(mistakes):
                print(f'GAME OVER! The secret word was "{secret_word}."')
                break
            
        display_game_state(mistakes, secret_word, guessed_letters)
        
    
        
        