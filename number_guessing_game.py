import random

logo = r"""
 ██████ ██    ███████████████████████    ██████████   █████████    ███    ████    █████    █████████ █████████████     
██      ██    ████     ██     ██            ██   ██   ████         ████   ████    ██████  ██████   ████     ██   ██    
██   █████    ███████  ██████████████       ██   ████████████      ██ ██  ████    ████ ████ ████████ █████  ██████     
██    ████    ████          ██     ██       ██   ██   ████         ██  ██ ████    ████  ██  ████   ████     ██   ██    
 ██████  ██████ █████████████████████       ██   ██   █████████    ██   ████ ██████ ██      ████████ █████████   ██    
                                                                                                                       
                                                                                                                       
"""


EASY_LEVEL = 10
HARD_LEVEL = 5

# Function to set difficulty
def set_difficulty():
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty == "easy":
            return EASY_LEVEL
        elif difficulty == "hard":
            return HARD_LEVEL
        else:
            print("Invalid input. Please try again!")

# Function to check user's guess against actual answer and returns
# the number of turns remaining
def check_answer(user_guess,turns, actual_answer):

    # Track the number of turns and reduce by 1
        if user_guess > actual_answer:
            print("Too high!" + "\n" + "Guess again.")
            return turns -1
        elif user_guess < actual_answer:
            print("Too low!" + "\n" + "Guess again.")
            return turns - 1
        else:
            print(f"You got it right. The answer is {actual_answer}")
            return turns - 1

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")

    # Choose a random number between 1 and 100
    answer = random.randint(1,100)
    print("I'm thinking of a number between 1 and 100.")

    attempt = set_difficulty()


    guess = 0

    # Repeat the guessing functionality if they get it wrong
    while guess != answer:
        print(f"You have {attempt} attempts to guess the number.")

        # Let the user guess a number
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempt = check_answer(guess,attempt,answer)

        if attempt == 0:
            print(f"You've run out of attempts. The number was {answer}.")
            return



gaming = True
while gaming:
    number_guessing_game = input("Will you like to play the Number Guessing Game. "
                             "Type 'y' for yes or 'n' for no: ")
    if number_guessing_game.lower() in "y":
        game()
    else:
        gaming = False