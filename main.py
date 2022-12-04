from art import logo
import random

print(logo)

number = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy or 'hard': ").lower()
if difficulty == 'hard':
    lives = 5
else:
    lives = 10



