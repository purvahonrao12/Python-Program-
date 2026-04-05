import random

def number_guessing_game():
    print(" Welcome to Number Guessing Game!")

    while True:
        number = random.randint(1, 100)
        attempts = 0
        max_attempts = 5

        print("\nI have selected a number between 1 and 100.")
        print("You have 5 attempts to guess it.")

        while attempts < max_attempts:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess == number:
                print(f" Correct! You guessed it in {attempts} attempts.")
                break
            elif guess < number:
                print("Too low!")
            else:
                print("Too high!")

        if guess != number:
            print(f" Game Over! The number was {number}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

number_guessing_game()