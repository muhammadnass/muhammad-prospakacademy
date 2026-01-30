"""
Simple Game with math and random Modules
An enhanced number guessing game with dynamic mathematical hints
and contextual feedback.
"""

import random
import math

def main():
    # Game Setup
    secret_number = random.randint(1, 100)
    max_guesses = 7
    guesses_taken = 0
    last_guess = None

    print("--- Welcome to the Enhanced Guessing Game! ---")
    print(f"I'm thinking of a number between 1 and 100. You have {max_guesses} attempts.")

    # Game Loop
    while guesses_taken < max_guesses:
        guess_str = input("\nGuess a number between 1 and 100 (or type 'hint'): ").strip().lower()

        # Enhancement 2: Contextual Hints with random.choice
        if guess_str == "hint":
            if last_guess is None:
                print("You need to make at least one guess before asking for a contextual hint!")
                continue
            
            if last_guess < secret_number:
                hints = [
                    "It's higher than your last guess!",
                    "The number is in the upper half of the remaining range.",
                    "Try adding 10 to your previous guess."
                ]
            else:
                hints = [
                    "It's lower than your last guess!",
                    "The number is in the lower half of the remaining range.",
                    "Try subtracting 5 from your previous guess."
                ]
            
            print(f"Here's a hint: {random.choice(hints)}")
            # Following instruction: 'hint' costs a guess for simplicity
            guesses_taken += 1
            print(f"Guesses used: {guesses_taken}/{max_guesses}")
            continue

        # Input Validation
        try:
            guess = int(guess_str)
        except ValueError:
            print("Error: Invalid input. Please enter a valid number or 'hint'.")
            continue

        guesses_taken += 1
        last_guess = guess

        # Compare guess to secret_number
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {guesses_taken} guesses!")
            break

        # Enhancement 1: Dynamic Hints with math
        # Offer a math hint if the user has made at least 3 guesses and hasn't won
        if guesses_taken >= 3 and guess != secret_number:
            sqrt_hint = math.floor(math.sqrt(secret_number))
            print(f"Hint: The integer part of the square root of the number is around {sqrt_hint}.")

    # Game End check
    if last_guess != secret_number:
        print(f"\nSorry, you ran out of guesses. The number was {secret_number}.")

if __name__ == "__main__":
    main()