import random
from colorama import Fore
from ascii_art import STAGES


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def display_game_state(state_of_the_game, color="RESET"):
    """Print state of the game."""
    secret_word = state_of_the_game["secret word"]
    guessed_letters = state_of_the_game["guessed letters"]
    mistakes = state_of_the_game["mistakes"]

    # Display the snowman stage for the current number of mistakes.
    print(Fore.BLUE + STAGES[mistakes])

    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(getattr(Fore, color) + "Word: " + display_word)
    print("\n")


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def is_game_won(guessed_letters, secret_word):
    """
    Check for winning condition:
    All secret world letters are guessed.
    """
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True


def is_game_lost(mistakes):
    """
    Check for losing condition:
    last stage reached.
    """
    if mistakes == len(STAGES):
        return True
    return False


def game_init():
    """
    Print welcome, chose secret word, initialize variables.
    Display init state.
    """
    print("Welcome to Snowman Meltdown!")
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    state_of_the_game = {
        "mistakes" : mistakes,
        "secret word" : secret_word,
        "guessed letters" : guessed_letters
        }

    display_game_state(state_of_the_game)
    return state_of_the_game


def get_valid_letter(state_of_the_game):
    """
    Promt the user for a letter and validates input.
    Return validated letter.
    """
    while True:
         # Prompt user for one guess (logic to be enhanced later)
        guess = input("Guess a letter: ").lower()
        guessed_letters = state_of_the_game["guessed letters"]

        if guess in guessed_letters:
            print(Fore.RED + f'You already guessed "{guess}".')
            continue

        if len(guess) != 1:
            print(Fore.RED + "Input must be a single letter!\n")
            continue

        if not guess.isalpha():
            print(Fore.RED + "Input must be a letter!\n")
            continue

        print("You guessed:", guess)
        return guess


def process_guess(guess, state_of_the_game):
    """
    Checks if letter is in secret word and winning/losing conditions.
    Switches colors in display accordingly
    """
    secret_word = state_of_the_game["secret word"]
    guessed_letters = state_of_the_game["guessed letters"]

    if guess in secret_word:
        guessed_letters.append(guess)
        color = "GREEN"

        if is_game_won(guessed_letters, secret_word):
            display_game_state(state_of_the_game, color)
            print(getattr(Fore, color) + "GAME WON!")
            return "game over"
    else:
        state_of_the_game["mistakes"] += 1
        color = "RED"

        if is_game_lost(state_of_the_game["mistakes"]):
            print(getattr(Fore, color) +
                  f'GAME OVER! The secret word was "{secret_word}".')
            return "game over"

    display_game_state(state_of_the_game, color)
    return "go on"


def check_for_continue():
    """
    Asks the player if they want to play another game.
    """
    while True:
        continue_game = input("\nCare for another try? (Y)es or (N)o?    ").lower()
        if continue_game in ("y", "yes"):
            return "yes"
        elif continue_game in ("n", "no"):
            return "no"
        else:
            print("I did not understand this.")


def play_game():
    """Execute game logic and checks for winning/losing conditions."""
    #general game loop
    while True:
        state_of_the_game = game_init()
        # input loop
        while True:
            guess = get_valid_letter(state_of_the_game)
            result = process_guess(guess, state_of_the_game)
            if result == "game over":
                continue_game = check_for_continue()
                if continue_game == "no":
                    return    #ends game
                if continue_game == "yes":
                    break     #jumps back into game loop
