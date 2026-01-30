#This program is a number guessing game

import random  

def main():

    secret_number = random.randint(1, 100)
    
    num_guesses = 0
    
    print("I'm thinking of a number between 1 and 100.")

    
    while True:
        try:
            
            user_guess = int(input("Guess the number (1-100): "))
            
            
            num_guesses += 1
            
            if user_guess < secret_number:
                print("Too low! Try again.")
                
            elif user_guess > secret_number:
                print("Too high! Try again.")
                
            else:
                
                print(f"Congratulations! You guessed it in {num_guesses} attempts!")
                
                break 

        except ValueError:

            print("Invalid input. Please enter a whole number.")

if __name__ == "__main__":
    main()