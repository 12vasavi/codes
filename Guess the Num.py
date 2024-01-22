import random
from art import logo

# Define the number of turns for the hard and easy levels
hard_level_turns = 5
easy_level_turns = 10

# Generate a random number between 1 and 50
number = random.randint(1, 50)

# Function to check user's guess against the actual answer.
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

# Function to set the game difficulty and return the number of turns accordingly.
def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return easy_level_turns
    else:
        return hard_level_turns

# The main game function
def game():
    print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 to 50. Can you guess it?")
    
    # For testing purposes (optional)
    print(f"Psst the number is {number}")

    # Set the difficulty level and initialize the number of chances
    chances = set_difficulty()
    guess = 0

    while guess != number:
        print(f"You have {chances} chances remaining to guess the number.")

        # Get user input for their guess
        guess = int(input("Make a guess: "))

        # Check the user's guess against the actual answer and update the remaining chances
        chances = check_answer(guess, number, chances)

        # If the player has run out of chances, end the game and display the correct answer
        if chances == 0:
            print("You've run out of guesses, you lose.")
            return
        # If the user's guess is incorrect, allow them to guess again
        elif guess != number:
            print("Guess again.")

# Start the game
game()
