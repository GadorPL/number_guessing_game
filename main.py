from art import logo
import random


def game_over(player_lives, player_guess, num):
    if player_lives == 0:
        return True, print("You lost.")
    elif player_guess == num:
        return True, print(f"You got it! The answer was {num}.")
    else:
        return False


def game():
    keep_playing = True
    while keep_playing:
        print(logo)
        print("Welcome to the Number Guessing Game!")

        number = random.randint(1, 100)
        difficulty = input("Choose a difficulty. Type 'easy or 'hard': ").lower()
        if difficulty == 'hard':
            lives = 5
        else:
            lives = 10

        print(f"You have {lives} attempts remaining to guess the number.")

        guess = 0
        while not game_over(lives, guess, number):
            guess = int(input("Make a guess: "))
            if guess != number:
                lives -= 1
                if guess > number:
                    print("Too high.")
                elif guess < number:
                    print("Too low.")
                print("Guess again.")
        restart_game = input("Do you want to play again? Type 'y' for yes or 'n' for no:  ").lower()
        if restart_game == 'y':
            game()
        else:
            print("Thanks for playing!")
            keep_playing = False


game()

