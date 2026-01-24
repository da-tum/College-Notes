import random

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Make a guess: "))
            attempts += 1
            if guess < 1 or guess > 100:
                print("Please guess a number within the range 1 to 100.")
                continue
        except ValueError:
            print("Oops! That doesn't look like a valid number. Please try again.")
            continue
        
        if guess < number_to_guess:
            print("Too low. Try again!")
        elif guess > number_to_guess:
            print("Too high. Try again!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

def main():
    while True:
        play_again = input("Would you like to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye!")
            break
        else:
            play_game()

if __name__ == "__main__":
    main()
