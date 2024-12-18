import random

def guess_number():
    print("Hello! I've chosen a number between 1 and 100. Try to guess it!")
    
    # Choose a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        # User input
        guess = input("Enter your guess: ")
        
        # Check if input is a valid number
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess)
        attempts += 1
        
        # Compare with the secret number
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

# Start the game
guess_number()
