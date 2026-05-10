import random
from colorama import Fore
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def display_game_state(mistakes, secret_word, guessed_letters, color="RESET"):
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


def play_game():
    """Execute game logic and checks for winning/losing conditions."""
    print("Welcome to Snowman Meltdown!")
    #general game loop
    while True:
        secret_word = get_random_word()
        guessed_letters = []
        mistakes = 0

        # For now, display the initial game state.
        display_game_state(mistakes, secret_word, guessed_letters)
        # input loop
        while True:
             # Prompt user for one guess (logic to be enhanced later)
            guess = input("Guess a letter: ").lower()
        
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
    
            if guess in secret_word:
                guessed_letters.append(guess)
                color = "GREEN"
                if is_game_won(guessed_letters, secret_word):
                    display_game_state(mistakes, secret_word, guessed_letters, color)
                    print(getattr(Fore, color) + f'GAME WON!')
                    break
            else:
                mistakes += 1
                color = "RED"
                if is_game_lost(mistakes):
                    print(getattr(Fore, color) + f'GAME OVER! The secret word was "{secret_word}."')
                    break
            
            display_game_state(mistakes, secret_word, guessed_letters, color)
        # continue game loop    
        while True:    
            continue_game = input("\nCare for another try? (Y)es or (N)o?    ").lower()
            if continue_game in ("y", "yes"):
                break    #breaks this loop, jumps into game loop
            elif continue_game in ("n", "no"):
                return    #end all loops 
            else:
                print("I did not understand this.")
            
    