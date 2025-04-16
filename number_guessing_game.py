import random

logo = r"""
 ██████ ██    ███████████████████████    ██████████   █████████    ███    ████    █████    █████████ █████████████     
██      ██    ████     ██     ██            ██   ██   ████         ████   ████    ██████  ██████   ████     ██   ██    
██   █████    ███████  ██████████████       ██   ████████████      ██ ██  ████    ████ ████ ████████ █████  ██████     
██    ████    ████          ██     ██       ██   ██   ████         ██  ██ ████    ████  ██  ████   ████     ██   ██    
 ██████  ██████ █████████████████████       ██   ██   █████████    ██   ████ ██████ ██      ████████ █████████   ██    
                                                                                                                       
                                                                                                                       
"""

print(logo)

def number_guessing_game():
    number_guessing = True
    while number_guessing:
        print("Welcome to the Number Guessing Game")
        print("I am thinking of a number between 1 and 100.")
        difficulty = input("choose a difficulty. Type 'easy' or 'hard': ").lower()
        attempts = 0
        numbers = list(range(1,100))

        random_number = random.choice(numbers)

        """Set attempt base on difficulty"""
        if difficulty == 'easy':
            attempts = 10
        elif difficulty == 'hard':
            attempts = 5

        gaming = True
        while gaming:
            print(f"You have {attempts} attempts remaining to guess the number.")

            guess = int(input("Make a guess: "))



            if guess > random_number:
                attempts -=1
                print("too high" + "\n" + "Guess again")
            elif guess < random_number:
                attempts -= 1
                print("too low" + "\n" + "Guess again")
            elif guess == random_number:
                print("You win!")
                gaming = False
            if attempts == 0:
                print(f"You run out of guesses, you lose.")
                gaming = False

        question = input("Type 'y' to play again, 'exit' to stop the game: ").lower()
        if question == 'y':
            print("Starting a new game...")
            number_guessing = True # Start a new game loop
        elif question == 'exit':
            print("Thanks for playing! Goodbye.")
            number_guessing = False
number_guessing_game()